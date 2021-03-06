# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='flut',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flutter_twitterclone.User'),
        ),
    ]
