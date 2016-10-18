# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_pinteam'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='baseuser',
            managers=[
                ('objects', accounts.models.NewUserManager()),
            ],
        ),
    ]
