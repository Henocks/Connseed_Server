# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 12:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoRaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Ppm', models.FloatField()),
                ('Wtr', models.IntegerField()),
                ('Lux', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoRaDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EUI', models.TextField(max_length=255)),
                ('Battery', models.IntegerField()),
                ('Nickname', models.CharField(max_length=255)),
                ('FK_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoRaStatisticalData_Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Ppm', models.FloatField()),
                ('Wtr', models.IntegerField()),
                ('Lux', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('FK_Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.LoRaDevice')),
            ],
        ),
        migrations.CreateModel(
            name='LoRaStatisticalData_Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Ppm', models.FloatField()),
                ('Wtr', models.IntegerField()),
                ('Lux', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('FK_Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.LoRaDevice')),
            ],
        ),
        migrations.CreateModel(
            name='LoRaStatisticalData_Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('Ppm', models.FloatField()),
                ('Wtr', models.IntegerField()),
                ('Lux', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('FK_Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.LoRaDevice')),
            ],
        ),
        migrations.AddField(
            model_name='loradata',
            name='FK_Device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.LoRaDevice'),
        ),
    ]
