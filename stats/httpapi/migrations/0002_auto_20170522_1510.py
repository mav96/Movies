# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='film',
            field=models.CharField(max_length=100),
        ),
    ]
