# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170108_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='token_number',
            field=models.CharField(null=True, max_length=1024, blank=True),
        ),
    ]
