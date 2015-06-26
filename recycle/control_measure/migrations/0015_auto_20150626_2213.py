# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0014_measurement_measurement_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_volume',
            field=models.IntegerField(blank='True', null='True', verbose_name='Объём в литрах'),
        ),
    ]
