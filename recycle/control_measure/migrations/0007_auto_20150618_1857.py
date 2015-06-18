# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0006_bin_bin_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measurement_bin',
            field=models.ForeignKey(to='control_measure.Bin', verbose_name='Контейнер'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_date',
            field=models.DateTimeField(verbose_name='Дата замера'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_percentage',
            field=models.DecimalField(default=50, decimal_places=1, verbose_name='Процент', max_digits=3),
        ),
    ]
