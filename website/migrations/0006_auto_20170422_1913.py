# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-22 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170422_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.CharField(choices=[('C', 'Corporate Sponsor'), ('I', 'Individual Sponsor')], max_length=15, verbose_name='sponsor type'),
        ),
    ]
