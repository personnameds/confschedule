# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 01:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Klass_Schedule_Details',
            new_name='KlassScheduleDetails',
        ),
        migrations.RenameModel(
            old_name='School_Schedule_Details',
            new_name='SchoolScheduleDetails',
        ),
        migrations.AlterModelOptions(
            name='klass',
            options={'verbose_name': 'Class'},
        ),
    ]
