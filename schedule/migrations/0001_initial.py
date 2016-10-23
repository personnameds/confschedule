# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=3)),
                ('grade', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Klass_Schedule_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pm_slots', models.PositiveSmallIntegerField(blank=True)),
                ('num_am_slots', models.PositiveSmallIntegerField(blank=True)),
                ('slot_length', models.PositiveSmallIntegerField(blank=True)),
                ('am_start', models.TimeField(blank=True)),
                ('pm_start', models.TimeField(blank=True)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Klass')),
            ],
        ),
        migrations.CreateModel(
            name='School_Schedule_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pm_slots', models.PositiveSmallIntegerField()),
                ('num_am_slots', models.PositiveSmallIntegerField()),
                ('slot_length', models.PositiveSmallIntegerField()),
                ('am_start', models.TimeField()),
                ('pm_start', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('am_pm', models.CharField(max_length=2)),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Klass')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Klass')),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='student',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Student'),
        ),
    ]