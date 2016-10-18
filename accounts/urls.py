from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import index_page, login, check_work

urlpatterns = [
    url(r'^index/', index_page, name="index"),
    url(r'^login/',  login, name="login" ),
    url(r'^check/',  check_work),

]
