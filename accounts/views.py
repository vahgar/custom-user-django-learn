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
from .forms import AuthenticationForm, RegistrationForm, AuthenticationFormPinteam
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.core import serializers


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


def pinteam_index(request):
    if(request.user.is_authenticated()):
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


def info_school_admin(request, school_id):
    school = School.objects.get(school_id=school_id)
    SchoolAdmins = SchoolAdmin.objects.filter(school=school)
    school_admin_list = []
    for i in SchoolAdmins:
        school_admin_list.append({'Name':i.first_name,'email':i.email,'school':i.school.school_name})
    print(school_admin_list)
    data = json.dumps(school_admin_list,indent=4)
    return HttpResponse(data, content_type='application/json')
