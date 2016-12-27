# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20161018_2021'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='studentuser',
            managers=[
                ('objects', accounts.models.NewUserManager()),
            ],
        ),
    ]
