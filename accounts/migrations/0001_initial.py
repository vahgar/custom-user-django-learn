# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.NewUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAdmin',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.ManagerForUser()),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('address', models.CharField(max_length=500, blank=True)),
                ('city', models.CharField(max_length=50, blank=True, null=True)),
                ('state', models.CharField(max_length=50, blank=True, null=True)),
                ('pincode', models.CharField(max_length=6, blank=True, null=True)),
                ('email_id', models.EmailField(max_length=254, blank=True)),
                ('phone_number', models.CharField(max_length=10, blank=True, null=True)),
                ('mother_phone', models.CharField(max_length=10, blank=True, null=True)),
                ('father_phone', models.CharField(max_length=10, blank=True, null=True)),
                ('standard', models.CharField(max_length=2, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.ManagerForUser()),
            ],
        ),
        migrations.AddField(
            model_name='baseuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_name='user_set', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set', verbose_name='user permissions'),
        ),
    ]
