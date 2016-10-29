# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classlists', '0003_auto_20161012_2009'),
        ('schedule', '0006_auto_20161010_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='KlassScheduleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pm_slots', models.PositiveSmallIntegerField(blank=True)),
                ('num_am_slots', models.PositiveSmallIntegerField(blank=True)),
                ('slot_length', models.PositiveSmallIntegerField(blank=True)),
                ('am_start', models.TimeField(blank=True)),
                ('pm_start', models.TimeField(blank=True)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classlists.Klass')),
            ],
            options={
                'verbose_name': 'Class Schedule',
                'verbose_name_plural': 'Class Schedules',
            },
        ),
    ]