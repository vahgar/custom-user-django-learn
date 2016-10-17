from accounts.models import BaseUSER, SchoolAdmin, Pinteam
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend


class BackendForAdmin(object):
    print("We are at Backend for admin")
    def authenticate(self, username=None, password=None):
        try:
            school_admin = SchoolAdmin.objects.get(email=username)
        except SchoolAdmin.DoesNotExist:
            return None

        if school_admin.check_password(password):
            return school_admin
        else:
            return None

    def get_user(self, email):
        try:
            return SchoolAdmin.objects.get(email=email)
        except SchoolAdmin.DoesNotExist:
            return None

class BackendForPinteam(object):
    print("We are at Backend for Pinteam")
    def authenticate(self, username=None, password=None):
        try:
            member = Pinteam.objects.get(email=username)
        except SchoolAdmin.DoesNotExist:
            return None

        if member.check_password(password):
            return member
        else:
            return None

    def get_user(self, email):
        try:
            return Pinteam.objects.get(email=email)
        except Pinteam.DoesNotExist:
            return None
