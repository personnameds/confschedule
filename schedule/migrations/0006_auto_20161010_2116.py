# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classlists.Student'),
        ),
    ]
