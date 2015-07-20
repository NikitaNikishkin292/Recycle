# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0021_measurement_measurement_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='measurement_error',
            field=models.DecimalField(decimal_places=1, blank='True', max_digits=3, verbose_name='Ошибка', null='True'),
        ),
    ]
