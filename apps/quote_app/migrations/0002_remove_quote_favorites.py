# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorites',
        ),
    ]
