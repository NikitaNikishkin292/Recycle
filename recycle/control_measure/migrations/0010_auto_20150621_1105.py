# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0009_type_type_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_percentage',
            field=models.DecimalField(max_digits=5, verbose_name='Процент', default=50, decimal_places=3),
        ),
    ]
