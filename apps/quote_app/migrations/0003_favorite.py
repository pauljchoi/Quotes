# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        ('quote_app', '0002_remove_quote_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote_app.Quote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.User')),
            ],
        ),
    ]
