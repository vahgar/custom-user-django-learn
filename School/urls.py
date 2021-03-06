from django.conf.urls import include, url
from django.contrib import admin
from School.api.api_views import SchoolCreateAPIView, SchoolStudentListAPIView, SchoolStudentClassListAPIView, SchoolListAPIView

urlpatterns = [
    url(r'^create/$', SchoolCreateAPIView.as_view(), name="school_create"),
    url(r'^list/$', SchoolListAPIView.as_view(), name="school_list"),
    url(r'^list/(?P<school_id>[0-9]+)/$', SchoolStudentListAPIView.as_view(), name="school_student_list"),
    url(r'^list/(?P<school_id>[0-9]+)/(?P<standard>[A-Z]+)/$', SchoolStudentClassListAPIView.as_view(), name="school_student_class_list"),

]
