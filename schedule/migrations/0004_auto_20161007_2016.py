# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20160913_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klassscheduledetails',
            name='klass',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='klass',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='klass',
        ),
        migrations.DeleteModel(
            name='Klass',
        ),
        migrations.DeleteModel(
            name='KlassScheduleDetails',
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
