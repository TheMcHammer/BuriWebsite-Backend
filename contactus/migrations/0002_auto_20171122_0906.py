# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(),
        ),
    ]
