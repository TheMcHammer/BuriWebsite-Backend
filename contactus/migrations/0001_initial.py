# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
    ]
