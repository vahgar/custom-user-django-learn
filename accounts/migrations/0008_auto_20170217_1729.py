# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170217_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='Standard',
            new_name='standard',
        ),
    ]
