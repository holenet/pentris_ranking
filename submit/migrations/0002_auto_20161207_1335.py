# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 04:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-score', 'submit_date', 'username']},
        ),
    ]
