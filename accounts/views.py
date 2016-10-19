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
from accounts.models import StudentUser, SchoolAdmin
from .forms import AuthenticationForm, RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index_page(request):
    print(request.session)
    if(request.user.is_authenticated()):
        user = request.user
        print(user)
        context = { 'user':user }
        return render(request,'accounts/login.html',context)
    else:
        print("No")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/index.html',context)


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
                    return render(request,'accounts/login.html',context)
                else:
                    return HttpResponse("Not Active")
            else:
                return HttpResponse("Please Check Your Credentials")
        else:
            return HttpResponse("Form is not valid")
    elif(request.user.is_authenticated()):
        user = request.user
        print(user)
        context = { 'user':user }
        return render(request,'accounts/login.html',context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/index.html',context)

@login_required
def check_work(request):
    x = request.user
    return HttpResponse(x)

@login_required
def logout(request):
    django_logout(request)
    return redirect('index_page')
