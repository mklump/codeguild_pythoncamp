# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter_twitterclone', '0002_flut_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flut',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]