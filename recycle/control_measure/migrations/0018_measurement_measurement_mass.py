# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0017_auto_20150628_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='measurement_mass',
            field=models.DecimalField(blank='True', max_digits=3, decimal_places=1, verbose_name='Масса PET', null='True'),
        ),
    ]
