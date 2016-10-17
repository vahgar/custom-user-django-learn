from django.db import models
from School.models import School
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.
class NewUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

class SuperManager(BaseUserManager):


    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


# USER STARTS HERE

class BaseUSER(AbstractBaseUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

class StudentUser(BaseUSER):

    student_id = models.CharField(primary_key=True,max_length=10)
    school = models.ForeignKey(School,blank=True,null=True)
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=6,blank=True, null=True)
    email_id =  models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    mother_phone = models.CharField(max_length=10, blank=True, null=True)
    father_phone = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=2,blank=True, null=True)
    # bus_transport = models.ForeignKey(Bus,blank=True,null=True)

    USERNAME_FIELD = 'student_id'


class SchoolAdmin(BaseUSER):

    school = models.ForeignKey(School,blank=True,null=True)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'

class Pinteam(BaseUSER):

    pin_level = models.CharField(max_length=10)


    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def is_superuser(self):
        return self.is_admin

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = SuperManager()

    USERNAME_FIELD = 'email'
