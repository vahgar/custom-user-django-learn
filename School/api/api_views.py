from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from rest_framework import parsers, renderers
from rest_framework.parsers import JSONParser
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from School.api.serializers import SchoolCreateSerializer
from School.models import School
from accounts.models import StudentUser

class SchoolCreateAPIView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolCreateSerializer

    permission_classes = [IsAuthenticated]
