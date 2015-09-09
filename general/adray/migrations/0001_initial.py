# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('clientID', models.CharField(max_length=30)),
                ('clientName', models.CharField(max_length=30)),
                ('credentials', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='datelocationchannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('clientID', models.CharField(max_length=30)),
                ('clientName', models.CharField(max_length=30)),
                ('channelName', models.CharField(max_length=30)),
                ('locationID', models.CharField(max_length=30)),
                ('locationName', models.CharField(max_length=30)),
                ('costCount', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='dateLocationResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('locationID', models.CharField(max_length=30)),
                ('SuccessCount', models.CharField(max_length=30)),
                ('clientID', models.CharField(max_length=30)),
                ('clientName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='geographyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('geoID', models.CharField(max_length=30)),
                ('granLevel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='testData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('TestName', models.CharField(max_length=30)),
                ('clientID', models.CharField(max_length=30)),
                ('clientName', models.CharField(max_length=30)),
                ('selectedChannel', models.CharField(max_length=30)),
                ('testStatus', models.CharField(max_length=30)),
                ('actionToDo', models.CharField(max_length=30)),
                ('successMetric', models.CharField(max_length=30)),
                ('StartDate', models.DateField(max_length=30)),
                ('endDate', models.DateField(max_length=30)),
                ('significance', models.DateField(max_length=30)),
                ('power', models.DateField(max_length=30)),
                ('totalAvailableGeos', models.CharField(max_length=30)),
                ('selectedGeos', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='testdateDataArcive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(max_length=30)),
                ('TestName', models.CharField(max_length=30)),
                ('clientID', models.CharField(max_length=30)),
                ('clientName', models.CharField(max_length=30)),
                ('selectedChannel', models.CharField(max_length=30)),
                ('testStatus', models.CharField(max_length=30)),
                ('actionToDo', models.CharField(max_length=30)),
                ('successMetric', models.CharField(max_length=30)),
                ('StartDate', models.DateField(max_length=30)),
                ('endDate', models.DateField(max_length=30)),
                ('significance', models.DateField(max_length=30)),
                ('power', models.DateField(max_length=30)),
                ('totalAvailableGeos', models.CharField(max_length=30)),
                ('selectedGeos', models.CharField(max_length=30)),
            ],
        ),
    ]
