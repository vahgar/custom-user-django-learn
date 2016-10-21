This a Project on How to Use Multiple Users in Django.

Welcome to the custom-user-django-learn wiki!

This is in order to explain How to use more Customer Users in django.

First of all in your models.py file create a Custom User By extending django's AbstractBaseUser, if you don't want username in your model else you can use AbstractUser if you need username. This wiki has AbstractBaseUser inherited.


    from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )
