from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework import parsers, renderers
from rest_framework.parsers import JSONParser
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Q
from School.api.serializers import SchoolCreateSerializer, StudentUserSerializer
from School.models import School
from accounts.models import StudentUser

class SchoolListAPIView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolCreateSerializer



class SchoolCreateAPIView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolCreateSerializer

    permission_classes = [IsAuthenticated]

class SchoolStudentListAPIView(ListAPIView):
    serializer_class = StudentUserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        school = self.kwargs['school_id']
        return StudentUser.objects.filter(school=school)


class SchoolStudentClassListAPIView(ListAPIView):
    serializer_class = StudentUserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        school = self.kwargs['school_id']
        standard = self.kwargs['standard']
        f1 = Q(school=school)
        f2 = Q(standard=standard)
        return StudentUser.objects.filter(f1 & f2)
