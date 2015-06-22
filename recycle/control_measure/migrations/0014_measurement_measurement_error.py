# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0013_measurement_measurement_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='measurement_error',
            field=models.DecimalField(max_digits=3, blank='True', verbose_name='Ошибка', null='True', decimal_places=1),
        ),
    ]
