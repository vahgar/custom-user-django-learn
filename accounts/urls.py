from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import index_page, login, check_work, logout, pinteam_index

urlpatterns = [
    url(r'^index/', index_page, name="index"),
    url(r'^login/',  login, name="login" ),
    url(r'^check/',  check_work),
    url(r'^logout/', logout),
    url(r'^pinteam/', pinteam_index),


]
