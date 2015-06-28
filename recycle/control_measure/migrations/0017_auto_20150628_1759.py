# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0016_remove_measurement_measurement_error'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='measurement_cells_inside',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='measurement_cells_maximum',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_percentage',
            field=models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Процент', default=50),
        ),
    ]
