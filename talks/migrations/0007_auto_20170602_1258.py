# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-02 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0006_auto_20170602_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='experience_level',
            field=models.CharField(choices=[('B', 'Beginner, no prior knowledge of Python required'), ('A', 'Average, some prior knowledge of Python required'), ('G', 'Good Python programmers level'), ('E', 'Experienced Python programmers level')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='talk_type',
            field=models.CharField(choices=[('Keynote', 'Keynote Talk - 45 mins'), ('Short Talk', 'Short Talk - 30 mins'), ('Long Talk', 'Long Talk - 1 hour'), ('Tutorial', 'Tutorial - 2 hours or more')], max_length=20),
        ),
    ]
