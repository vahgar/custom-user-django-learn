# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_baseuser_token_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='token_number',
            field=models.CharField(blank=True, max_length=1024, null=True, unique=True),
        ),
    ]
