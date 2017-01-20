from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ManagerForUser(BaseUserManager):

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
        self.is_staff = False;
        return self._create_user(email, password, **extra_fields)

class ManagerForUser2(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, student_id, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not student_id:
            raise ValueError('The given student_id must be set')
        student_id = self.student_id
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        self.is_staff = False;
        return self._create_user(email, password, **extra_fields)




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
        self.is_staff = False;
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class BaseUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=True)
    token_number = models.CharField(max_length=1024,blank=True,null=True,unique=True)

    objects = NewUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.first_name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def __str__(self):
        return self.email

class StudentUser(BaseUser):

    student_id = models.CharField(primary_key=True,max_length=10)
    # school = models.ForeignKey(School,blank=True,null=True)
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=6,blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    mother_phone = models.CharField(max_length=10, blank=True, null=True)
    father_phone = models.CharField(max_length=10, blank=True, null=True)
    standard = models.CharField(max_length=2,blank=True, null=True)
    # bus_transport = models.ForeignKey(Bus,blank=True,null=True)


    objects = ManagerForUser2()

    USERNAME_FIELD = 'student_id'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.first_name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def __str__(self):
        return self.email

class SchoolAdmin(BaseUser):

    # school = models.ForeignKey(School,blank=True,null=True)

    objects = ManagerForUser()

    USERNAME_FIELD = 'email'

    def __str__(self):
        x = self.email
        return x
