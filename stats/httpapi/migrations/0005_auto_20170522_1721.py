# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpapi', '0004_auto_20170522_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='count_user',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='film',
            name='watch_time',
            field=models.FloatField(default=0.0),
        ),
    ]
