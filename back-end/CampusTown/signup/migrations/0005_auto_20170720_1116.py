# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20170720_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(max_length=10),
        ),
    ]
