from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import index_page, login, check_work, logout, pinteam_index, login_pinteam, info_school_admin
from accounts.api.api_views import BaseUserCreateAPIView, SchoolAdminCreateAPIView

urlpatterns = [
    url(r'^schooladmin/index/', index_page, name="index_page"),
    url(r'^schooladmin/login/',  login, name="login" ),
    url(r'^schooladmin/create$', SchoolAdminCreateAPIView.as_view(), name='admin_create'),
    url(r'^check/',  check_work),
    url(r'^logout/', logout),
    url(r'^pinteam/index/', pinteam_index),
    url(r'^pinteam/login/', login_pinteam, name="pin_login"),
    url(r'^pinteam/create$', BaseUserCreateAPIView.as_view(), name='pin_create'),


]
