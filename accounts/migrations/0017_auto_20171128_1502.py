# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20171121_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 28, 15, 2, 39, 687131)),
        ),
    ]