# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(blank=True, null=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='school',
            name='affiliation_number',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='board',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='pincode',
            field=models.CharField(blank=True, null=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_branch_area',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(blank=True, null=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='school',
            name='state',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='school',
            name='transport_incharge',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='transport_incharge_number',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='zone',
            field=models.CharField(choices=[('North', 'North'), ('East', 'East'), ('West', 'West'), ('South', 'South'), ('North East', 'North East'), ('Nort West', 'North West'), ('Central', 'Central'), ('New Delhi', 'New Delhi'), ('South West', 'South West')], blank=True, null=True, max_length=15),
        ),
    ]
