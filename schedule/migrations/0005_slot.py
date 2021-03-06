# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classlists', '0001_initial'),
        ('schedule', '0004_auto_20161007_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('am_pm', models.CharField(max_length=2)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classlists.Klass')),
                ('student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='classlists.Student')),
            ],
        ),
    ]
