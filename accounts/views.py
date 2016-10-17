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
from accounts.models import StudentUser
from .forms import AuthenticationForm, RegistrationForm

# Create your views here.
def index_page(request):

    if(request.user.is_authenticated()):
        user = request.user
        context = { 'user':user }
        return render(request,'accounts/login.html',context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/index.html',context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    school = user.school
                    q_set = StudentUser.objects.filter(school=school)
                    q_set_list = []
                    for i in q_set:
                        q_set_list.append(i)
                    context = { 'user':user, 'q_set_list':q_set_list }
                    return render(request,'accounts/login.html',context)
                else:
                    return HttpResponse("Not Active")
            else:
                return HttpResponse("None")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/index.html',context)
