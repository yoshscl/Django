# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adray', '0002_remove_testdata_selectedchannel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdata',
            name='power',
        ),
        migrations.RemoveField(
            model_name='testdata',
            name='significance',
        ),
    ]
