# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-07 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='location',
            name='neighborhood',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
