# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0026_bin_bin_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unload',
            name='unload_bins_list',
            field=models.ManyToManyField(blank='True', null='True', verbose_name='Выгружаемые контейнеры', to='control_measure.Bin'),
        ),
    ]
