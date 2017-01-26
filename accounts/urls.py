from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views
from accounts.views import index_page, login, check_work, logout, pinteam_index, login_pinteam, info_school_admin, student_index, student_login, student_token_index, createtoken_student
from accounts.api.api_views import BaseUserCreateAPIView, SchoolAdminCreateAPIView, UserListAPIView, StudentListAPIView

urlpatterns = [
    url(r'^schooladmin/index/', index_page, name="index_page"),
    url(r'^schooladmin/login/',  login, name="login" ),
    url(r'^schooladmin/create$', SchoolAdminCreateAPIView.as_view(), name='admin_create'),
    url(r'^check/',  check_work),
    url(r'^logout/', logout),
    url(r'^pinteam/index/', pinteam_index),
    url(r'^pinteam/login/', login_pinteam, name="pin_login"),
    url(r'^pinteam/create$', BaseUserCreateAPIView.as_view(), name='pin_create'),
    url(r'^list/$', UserListAPIView.as_view(), name='list_view'),
    url(r'^studentuser/index/', student_index, name="student_index"),
    url(r'^studentuser/login/', student_login, name="student_login"),
    url(r'^studentuser/token/', student_token_index, name="token"),
    # url(r'^studentuser/createtoken/', StudentCreateTokenAPIView.as_view(), name="createstudent_token"),
    url(r'^studentuser/(?P<student_id>[0-9]+)/$',StudentListAPIView.as_view(), name="detail_student"),
    url(r'^api-token-auth/', views.obtain_auth_token),
    




]
