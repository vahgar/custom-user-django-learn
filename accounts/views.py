# from django.shortcuts import render
# from django.http import HttpResponse
# from accounts.forms import RegistrationForm, AuthenticationForm
# from School.models import School
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login, logout, authenticate
# from django.views.decorators.http import require_http_methods, require_GET, require_POST
# from accounts.models import SchoolAdmin
from django.shortcuts import render_to_response, redirect, render, HttpResponse
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from accounts.models import StudentUser, SchoolAdmin, BaseUser
from School.models import School
from .forms import AuthenticationForm, RegistrationForm, AuthenticationFormPinteam, AuthenticationFormStudent
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from rest_framework.authtoken.models import Token
from django.core import serializers
from .backends import BackendForStudents


# Create your views here.

def index_page(request):
    if(request.user.is_authenticated()):
        name = request.user.email
        try:
            check = SchoolAdmin.objects.get(email=name)
        except SchoolAdmin.DoesNotExist:
            django_logout(request)
            form = AuthenticationForm()
            context = {'form':form}
            return render(request,'accounts/SchoolAdmin/index.html',context)
        user = request.user
        print(user)
        context = { 'user':user }
        return render(request,'accounts/SchoolAdmin/login.html',context)
    else:
        print("No")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/SchoolAdmin/index.html',context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['email']
            try:
                check = SchoolAdmin.objects.get(email=name)
            except SchoolAdmin.DoesNotExist:
                return HttpResponse("User Does Not Exists")
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    school = check.school
                    q_set = StudentUser.objects.filter(school=school)
                    q_set_list = []
                    for i in q_set:
                        q_set_list.append(i)
                    context = { 'user':user,'q_set_list':q_set_list}
                    return render(request,'accounts/SchoolAdmin/login.html',context)
                else:
                    return HttpResponse("Not Active")
            else:
                return HttpResponse("Please Check Your Credentials")
        else:
            return HttpResponse("Form is not valid")
    elif(request.user.is_authenticated()):
        user = request.user
        email = user.email
        check = SchoolAdmin.objects.get(email=email)
        school = check.school
        q_set = StudentUser.objects.filter(school=school)
        q_set_list = []
        for i in q_set:
            q_set_list.append(i)
        context = { 'user':user,'q_set_list':q_set_list}
        return render(request,'accounts/SchoolAdmin/login.html',context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/SchoolAdmin/index.html',context)

@login_required
def check_work(request):
    x = request.user
    return HttpResponse(x)

@login_required
def logout(request):
    django_logout(request)
    return redirect('index_page')

''' Pin team Index & Login '''
def pinteam_index(request):
    if(request.user.is_authenticated()):
        name = request.user.email
        try:
            check = SchoolAdmin.objects.get(email=name)
            django_logout(request)
            form = AuthenticationForm()
            context = {'form':form}
            return render(request,'accounts/Pinteam/index.html',context)
        except SchoolAdmin.DoesNotExist:
            user = request.user
            schools = School.objects.all()
            school_list = []
            for i in schools:
                school_list.append(i)
            context = {'user':user,'school_list':school_list}
            return render(request,'accounts/Pinteam/login.html',context)
    else:
        print("Pin index")
        form = AuthenticationFormPinteam()
        context = {'form':form}
        return render(request,'accounts/Pinteam/index.html',context)


def login_pinteam(request):
    if request.method == 'POST':
        form = AuthenticationFormPinteam(request.POST)
        print("At pin view")
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                check = BaseUser.objects.get(email=email)
            except BaseUser.DoesNotExist:
                return HttpResponse("User Does Not Exists")
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    django_login(request,user)
                    schools = School.objects.all()
                    school_list = []
                    for i in schools:
                        school_list.append(i)
                    context = {'user':user,'school_list':school_list}
                    return render(request,'accounts/Pinteam/login.html',context)
                else:
                    return HttpResponse("Not Active")
            else:
                return HttpResponse("User Check Credentials")
        else:
            return HttpResponse("Form Not Valid")
    elif(request.user.is_authenticated()):
        name = request.user.email
        try:
            check = SchoolAdmin.objects.get(email=name)
            django_logout(request)
            form = AuthenticationForm()
            context = {'form':form}
            return render(request,'accounts/Pinteam/index.html',context)
        except SchoolAdmin.DoesNotExist:
            user = request.user
            schools = School.objects.all()
            school_list = []
            for i in schools:
                school_list.append(i)
            context = {'user':user,'school_list':school_list}
            return render(request,'accounts/Pinteam/login.html',context)
    else:
        form = AuthenticationFormPinteam()
        context = {'form':form}
        return render(request,'accounts/Pinteam/index.html',context)

''' Pin team Ends '''

def info_school_admin(request, school_id):
    school = School.objects.get(school_id=school_id)
    SchoolAdmins = SchoolAdmin.objects.filter(school=school)
    school_admin_list = []
    for i in SchoolAdmins:
        school_admin_list.append({'Name':i.first_name,'email':i.email,'school':i.school.school_name})
    print(school_admin_list)
    data = json.dumps(school_admin_list,indent=4)
    return HttpResponse(data, content_type='application/json')

def student_index(request):
    print("At Student Index")
    if(request.user.is_authenticated()):
        name = request.user.student_id
        try:
            check = StudentUser.objects.get(student_id=name)
        except StudentUser.DoesNotExist:
            django_logout(request)
            form = AuthenticationFormStudent()
            context = {'form':form}
            return render(request,'accounts/StudentUser/index.html',context)
        user = request.user
        print(user)
        context = { 'user':user }
        return render(request,'accounts/StudentUser/login.html',context)
    else:
        form = AuthenticationFormStudent()
        context = {'form':form}
        return render(request,'accounts/StudentUser/index.html',context)

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationFormStudent(request.POST)
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data['student_id']
            try:
                check = StudentUser.objects.get(student_id=name)
            except StudentUser.DoesNotExist:
                return HttpResponse("User Does Not Exists")
            user = authenticate(username=form.cleaned_data['student_id'], password=form.cleaned_data['password'])
            print(user)
            request.user = user
            print(request.user)
            if user is not None:
                if user.is_active:

                    django_login(request, user)
                    # school = check.school
                    # q_set = StudentUser.objects.filter(school=school)
                    # q_set_list = []
                    # for i in q_set:
                    #     q_set_list.append(i)
                    context = { 'user':user}
                    return render(request,'accounts/StudentUser/login.html',context)
                else:
                    return HttpResponse("Not Active")
            else:
                return HttpResponse("Please Check Your Credentials")
        else:
            return HttpResponse("Form is not valid")
    elif(request.user.is_authenticated()):
        user = request.user
        student_id = user.student_id
        check = SchoolAdmin.objects.get(student_id=email)
        school = check.school
        q_set = StudentUser.objects.filter(school=school)
        q_set_list = []
        for i in q_set:
            q_set_list.append(i)
        context = { 'user':user,'q_set_list':q_set_list}
        return render(request,'accounts/StudentUser/login.html',context)
    else:
        form = AuthenticationFormStudent()
        context = {'form':form}
        return render(request,'accounts/StudentUser/index.html',context)

def student_token_index(request):
    if(request.user.is_authenticated()):
        return HttpResponse("You need to Logout first")
    else:
        form = AuthenticationFormStudent()
        context = {'form':form}
        return render(request,'accounts/StudentUser/token_index.html',context)




def createtoken_student(request):
    if request.method == 'POST':
        form = AuthenticationFormStudent(request.POST)
        if form.is_valid():
            name = form.cleaned_data['student_id']
            try:
                check = StudentUser.objects.get(student_id=name)
            except StudentUser.DoesNotExist:
                return HttpResponse("User Does Not Exists")
            user = authenticate(username=form.cleaned_data['student_id'], password=form.cleaned_data['password'])
            if(user.is_authenticated()):
                token = Token.objects.get_or_create(user=user)
                token = Token.objects.get(user=user)
                response_data = {}
                response_data['student_id'] = name
                response_data['token'] = token.key

                return HttpResponse(json.dumps(response_data), content_type="application/json")
