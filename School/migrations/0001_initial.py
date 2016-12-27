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
                ('school_id', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('school_name', models.CharField(max_length=300, blank=True, null=True)),
                ('school_branch_area', models.CharField(max_length=200, blank=True, null=True)),
                ('affiliation_number', models.CharField(max_length=100, blank=True, null=True)),
                ('board', models.CharField(max_length=10, blank=True, null=True)),
                ('address', models.CharField(max_length=1000, blank=True, null=True)),
                ('zone', models.CharField(choices=[('North', 'North'), ('East', 'East'), ('West', 'West'), ('South', 'South'), ('North East', 'North East'), ('Nort West', 'North West'), ('Central', 'Central'), ('New Delhi', 'New Delhi'), ('South West', 'South West')], max_length=15, blank=True, null=True)),
                ('city', models.CharField(max_length=100, blank=True, null=True)),
                ('state', models.CharField(max_length=100, blank=True, null=True)),
                ('pincode', models.CharField(max_length=6, blank=True, null=True)),
                ('active_status', models.BooleanField(default=1)),
                ('transport_incharge', models.CharField(max_length=50, blank=True, null=True)),
                ('transport_incharge_number', models.CharField(max_length=10, blank=True, null=True)),
                ('check_filed', models.CharField(max_length=100, blank=True, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
