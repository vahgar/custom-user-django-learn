# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0004_studentuser_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='is_superuser',
        ),
        migrations.AddField(
            model_name='pinteam',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', related_name='user_set'),
        ),
        migrations.AddField(
            model_name='pinteam',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='pinteam',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', related_name='user_set'),
        ),
    ]
