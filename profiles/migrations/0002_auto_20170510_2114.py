# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-10 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(help_text='Tell us a bit about yourself and your work with Python', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, help_text='Please enter your date of birth in the format YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, help_text='Please include your country code.', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_username',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_page',
            field=models.CharField(blank=True, help_text='Your website/blog URL.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(help_text='City, Country', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
