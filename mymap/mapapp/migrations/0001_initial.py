# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-05 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(default=0, verbose_name='Longitude')),
                ('latitude', models.FloatField(default=0, verbose_name='Latitude')),
            ],
        ),
    ]