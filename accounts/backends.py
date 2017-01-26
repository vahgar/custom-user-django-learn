from accounts.models import BaseUser, SchoolAdmin, StudentUser
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend


class BackendForStudents(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            member = StudentUser.objects.get(student_id=username)
        except SchoolAdmin.DoesNotExist:
            return None

        if member.check_password(password):
            return member
        else:
            return None

    def get_user(self, student_id):
        try:
            return StudentUser.objects.get(student_id=student_id)
        except StudentUser.DoesNotExist:
            return None
