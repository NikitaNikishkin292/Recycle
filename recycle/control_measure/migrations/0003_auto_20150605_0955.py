# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='bin_adress',
            field=models.CharField(max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='bin',
            name='bin_id',
            field=models.IntegerField(verbose_name='Номер', default=1),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_date',
            field=models.DateTimeField(),
        ),
    ]
