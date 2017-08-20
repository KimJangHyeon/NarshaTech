# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20170816_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityinfo',
            name='category',
            field=models.CharField(choices=[('art/design', 'art/design'), ('fashion', 'fashion'), ('entertainment', 'entertainment'), ('sports', 'sports'), ('campustour', 'campustour'), ('well-being', 'well-being'), ('nature', 'nature'), ('food', 'food'), ('life style', 'life style'), ('history', 'history'), ('music', 'music'), ('business', 'business'), ('bar/club', 'bar/club')], default='art/design', max_length=30),
        ),
    ]
