# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0005_auto_20161017_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinteam',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='pinteam',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='pinteam',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', to='auth.Group', blank=True),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', related_query_name='user', to='auth.Permission', blank=True),
        ),
    ]
