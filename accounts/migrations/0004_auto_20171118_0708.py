# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20171118_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='inbox',
            field=models.CharField(default='Welcome to Our website', max_length=10000),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='sender',
            field=models.CharField(default='ADMIN', max_length=100),
        ),
    ]