# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-03 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_klassscheduledetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='not_available',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]