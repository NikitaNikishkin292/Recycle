# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0007_auto_20150618_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_cells_inside',
            field=models.DecimalField(null='True', decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_cells_maximum',
            field=models.DecimalField(null='True', decimal_places=1, max_digits=3),
        ),
    ]
