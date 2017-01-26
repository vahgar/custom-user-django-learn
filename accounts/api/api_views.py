from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework import parsers, renderers
from rest_framework.parsers import JSONParser
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from accounts.api.serializers import BaseUserCreateSerializer, SchoolAdminCreateSerializer, UserClass, StudentUserClass
from accounts.models import BaseUser, SchoolAdmin, StudentUser
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

class BaseUserCreateAPIView(CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserCreateSerializer

    permission_classes = [AllowAny]

class SchoolAdminCreateAPIView(CreateAPIView):
    queryset = SchoolAdmin.objects.all()
    serializer_class = SchoolAdminCreateSerializer
    permission_classes = [AllowAny]

class UserListAPIView(ListAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UserClass
    permission_classes = [AllowAny]

class StudentListAPIView(ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserClass
