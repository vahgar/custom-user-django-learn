# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='studentuser',
            managers=[
                ('objects', accounts.models.ManagerForUser2()),
            ],
        ),
        migrations.RemoveField(
            model_name='studentuser',
            name='email_id',
        ),
    ]
