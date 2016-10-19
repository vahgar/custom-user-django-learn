# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0012_baseuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinteam',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='pinteam',
            name='is_active',
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
            field=models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups', related_name='user_set', blank=True),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions', related_name='user_set', blank=True),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
