# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20161018_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
