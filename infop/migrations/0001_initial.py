# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 10:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default=None, max_length=100)),
                ('username', models.CharField(default=None, max_length=100)),
                ('email', models.CharField(default=None, max_length=100)),
                ('first_name', models.CharField(default=None, max_length=250)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('designation', models.CharField(default=None, max_length=500)),
                ('institute_name', models.CharField(default=None, max_length=100)),
                ('profile_photo', models.FileField(default=None, upload_to='')),
                ('phone_number', models.CharField(default=None, max_length=20)),
                ('about', models.CharField(default=None, max_length=500)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
