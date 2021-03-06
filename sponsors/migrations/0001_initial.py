# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-31 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='sponsor name')),
                ('category', models.CharField(choices=[('Bronze', 'Bronze - $500'), ('Silver', 'Silver - $1000'), ('Gold', 'Gold - $2000'), ('Platinum', 'Platinum - $5000')], max_length=15)),
                ('logo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('type', models.CharField(choices=[('C', 'Corporate Sponsor'), ('I', 'Individual Sponsor')], max_length=1, verbose_name='sponsor type')),
                ('website', models.CharField(blank=True, max_length=200, null=True, verbose_name='website URL/ Twitter handler')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
