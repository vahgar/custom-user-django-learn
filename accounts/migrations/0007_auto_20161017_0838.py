# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('accounts', '0006_auto_20161017_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinteam',
            name='baseuser_ptr',
        ),
        migrations.AlterModelManagers(
            name='baseuser',
            managers=[
                ('objects', accounts.models.SuperManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Pinteam',
        ),
    ]
