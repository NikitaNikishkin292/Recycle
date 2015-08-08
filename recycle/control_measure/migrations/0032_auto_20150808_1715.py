# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0031_auto_20150808_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_pace',
            name='city_pace_value',
            field=models.DecimalField(decimal_places=3, verbose_name='Темп м3/сутки', max_digits=6),
        ),
    ]
