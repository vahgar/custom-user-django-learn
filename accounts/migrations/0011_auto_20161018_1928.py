# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0010_baseuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='pinteam',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', related_query_name='user', blank=True, related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='pinteam',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pinteam',
            name='is_superuser',
            field=models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False),
        ),
        migrations.AddField(
            model_name='pinteam',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_query_name='user', blank=True, related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.'),
        ),
    ]
