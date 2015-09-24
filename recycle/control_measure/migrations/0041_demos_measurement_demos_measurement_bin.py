# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0040_auto_20150924_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='demos_measurement',
            name='demos_measurement_bin',
            field=models.ForeignKey(verbose_name='Измеренный контейнер', blank='True', to='control_measure.Bin', null='True'),
        ),
    ]
