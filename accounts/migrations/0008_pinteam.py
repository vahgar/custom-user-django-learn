# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20161017_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinteam',
            fields=[
                ('baseuser_ptr', models.OneToOneField(primary_key=True, parent_link=True, to=settings.AUTH_USER_MODEL, auto_created=True, serialize=False)),
                ('pin_level', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.SuperManager()),
            ],
        ),
    ]
