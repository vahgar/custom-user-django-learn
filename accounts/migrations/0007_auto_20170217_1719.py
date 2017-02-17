# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_studentuser_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='standard',
        ),
        migrations.AddField(
            model_name='studentuser',
            name='Standard',
            field=models.CharField(null=True, max_length=15, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('X', 'XI'), ('X', 'XII')], blank=True),
        ),
    ]
