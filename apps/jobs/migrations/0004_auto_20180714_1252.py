# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-14 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20180713_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
