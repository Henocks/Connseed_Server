# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loladata',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]
