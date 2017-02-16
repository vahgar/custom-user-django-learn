# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_auto_20170217_0044'),
        ('accounts', '0005_remove_baseuser_token_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='school',
            field=models.ForeignKey(to='School.School', blank=True, null=True),
        ),
    ]
