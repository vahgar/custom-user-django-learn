Welcome to the custom-user-django-learn wiki!

This is in order to explain "How to use Custom Users in django".

First of all in your models.py file create a Custom User By extending django's AbstractBaseUser, We are going to use AbstractBaseUser in this one as I do not want to include username field in my model.

For Better understanding read AbstractBaseUser model from link below. (https://github.com/django/django/blob/master/django/contrib/auth/base_user.py)

Import the 3 things below in your models.py


    from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )

Create your model as per requirement.

    class CustomUser(AbstractBaseUser, PermissionsMixin):

        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=30 )
        last_name = models.CharField(max_length=50, blank=True)
        is_staff = models.BooleanField(default=True)

We have Extended PermissionsMixin because it grants rights for user to Enter in default Admin Panel.

Now we need to know about Managers in Django. As the name suggests they manage the models.
Read About django's [BaseUserManager](https://github.com/django/django/blob/master/django/contrib/auth/base_user.py)

We will extend BaseUserManager to fill up Our requirement. You can do this in models.py file before defining your CustomUser Model.

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

      def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

Now we will add our NewUserManager to our CustomUser, for that we do:

    objects = NewUserManager()

Your CustomerUser will now look like:

    class CustomUser(AbstractBaseUser, PermissionsMixin):

        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=50, null=True, blank=True)
        last_name = models.CharField(max_length=50, null=True, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=True)

        objects = NewUserManager()

Now we will add USERNAME_FIELD to our CustomUser that will define what attribute will be used in place of username. Here it's email.

    class CustomUser(AbstractBaseUser, PermissionsMixin):

        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=50, null=True, blank=True)
        last_name = models.CharField(max_length=50, null=True, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=True)

        objects = NewUserManager()

        USERNAME_FIELD = 'email'

Now we will add 2 methods that are required when you log into Admin Panel (Copy & Paste it within CustomUser model)

    class CustomUser(AbstractBaseUser, PermissionsMixin):

        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=50, null=True, blank=True)
        last_name = models.CharField(max_length=50, null=True, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=True)

        objects = NewUserManager()

        USERNAME_FIELD = 'email'

        def get_full_name(self):
          return self.first_name

        def get_short_name(self):
          return self.first_name

Now go to your settings.py and add the following line of code.

    AUTH_USER_MODEL = 'myappname.CustomUser'

Now you are ready with one CustomUser Model without username.

I'll be soon adding how to use more than one Custom user model.
