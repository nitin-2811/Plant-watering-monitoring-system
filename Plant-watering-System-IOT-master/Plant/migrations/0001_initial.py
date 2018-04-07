# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 12:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 262347))),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(blank=True, max_length=100)),
                ('lat', models.FloatField(default=0.0)),
                ('lon', models.FloatField(default=0.0)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 246692))),
            ],
        ),
        migrations.CreateModel(
            name='Rain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_level', models.CharField(max_length=5)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 262347))),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_level', models.CharField(max_length=5)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 262347))),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.Plants')),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=20)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 262347))),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.Plants')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=5)),
                ('dt', models.DateTimeField(default=datetime.datetime(2017, 11, 3, 17, 49, 12, 262347))),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.User')),
            ],
        ),
        migrations.AddField(
            model_name='rain',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.User'),
        ),
        migrations.AddField(
            model_name='plants',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.User'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plant.Plants'),
        ),
    ]
