# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0011_auto_20150621_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_cells_inside',
            field=models.DecimalField(max_digits=3, decimal_places=1, null='True', blank='True'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_cells_maximum',
            field=models.DecimalField(max_digits=3, decimal_places=1, null='True', blank='True'),
        ),
    ]
