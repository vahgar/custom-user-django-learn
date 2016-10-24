from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import index_page, login, check_work, logout, pinteam_index, login_pinteam

urlpatterns = [
    url(r'^schooladmin/index/', index_page, name="index_page"),
    url(r'^schooladmin/login/',  login, name="login" ),
    url(r'^check/',  check_work),
    url(r'^logout/', logout),
    url(r'^pinteam/index/', pinteam_index),
    url(r'^pinteam/login/', login_pinteam, name="pin_login"),


]
