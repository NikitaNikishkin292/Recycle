# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0030_city_pace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_pace',
            name='city_pace_value',
            field=models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Темп м3/сутки'),
        ),
    ]
