# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20161017_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
