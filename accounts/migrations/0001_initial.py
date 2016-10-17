# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUSER',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50, blank=True, null=True)),
                ('last_name', models.CharField(max_length=50, blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pinteam',
            fields=[
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('pin_level', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.SuperManager()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolAdmin',
            fields=[
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('school', models.ForeignKey(blank=True, to='School.School', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.NewUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, to=settings.AUTH_USER_MODEL, parent_link=True)),
                ('student_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
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
        ),
    ]
