# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_quote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone_num', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('commodity_type', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=300)),
                ('packing_type', models.CharField(max_length=300)),
                ('is_clear_forward', models.BooleanField(default=False)),
                ('pick_from', models.CharField(max_length=300)),
                ('deliver_to', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='client',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='commodity',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Commodity',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
    ]
