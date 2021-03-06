# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-20 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talks', '0010_auto_20170602_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_day', models.CharField(choices=[('1', 'Day 1 - Workshops'), ('2', 'Day 2 - Talks'), ('3', 'Day 3 - Talks'), ('4', 'Day 4 - Sprints')], default='', max_length=1)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('talk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talks.Proposal')),
            ],
            options={
                'verbose_name_plural': 'talk Schedule',
                'managed': True,
            },
        ),
    ]
