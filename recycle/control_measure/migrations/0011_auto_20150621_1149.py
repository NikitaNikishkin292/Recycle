# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0010_auto_20150621_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_percentage',
            field=models.DecimalField(default=50, max_digits=3, decimal_places=1, verbose_name='Процент'),
        ),
    ]
