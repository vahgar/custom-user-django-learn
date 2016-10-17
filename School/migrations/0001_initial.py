# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('school_name', models.CharField(max_length=300)),
                ('school_branch_area', models.CharField(max_length=200)),
                ('affiliation_number', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=1000)),
                ('zone', models.CharField(max_length=15, choices=[('North', 'North'), ('East', 'East'), ('West', 'West'), ('South', 'South'), ('North East', 'North East'), ('Nort West', 'North West'), ('Central', 'Central'), ('New Delhi', 'New Delhi'), ('South West', 'South West')])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6)),
                ('active_status', models.BooleanField(default=1)),
                ('transport_incharge', models.CharField(max_length=50)),
                ('transport_incharge_number', models.CharField(max_length=10)),
                ('check_filed', models.CharField(max_length=100, blank=True, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
