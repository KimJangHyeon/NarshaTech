# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_auto_20170721_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='last_login',
        ),
    ]
