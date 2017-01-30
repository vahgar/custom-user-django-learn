# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170120_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='token_number',
        ),
    ]
