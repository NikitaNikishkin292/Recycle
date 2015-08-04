# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0023_bag_bag_in_bin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_error',
            field=models.DecimalField(null='True', decimal_places=1, verbose_name='Ошибка', blank='True', max_digits=4),
        ),
    ]
