from django.conf.urls import include, url
from django.contrib import admin
from School.api.api_views import SchoolCreateAPIView

urlpatterns = [
    url(r'^list/', SchoolCreateAPIView.as_view(), name="school_list"),

]
