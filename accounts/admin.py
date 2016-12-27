from django.contrib import admin
from .models import BaseUser, StudentUser, SchoolAdmin

from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(BaseUser)
admin.site.register(StudentUser)
admin.site.register(SchoolAdmin)
