# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_auto_20161017_0523'),
        ('accounts', '0003_baseuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='school',
            field=models.ForeignKey(to='School.School', null=True, blank=True),
        ),
    ]
