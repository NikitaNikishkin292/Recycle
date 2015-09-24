# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0038_auto_20150919_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='demos',
            name='demos_bins',
            field=models.ManyToManyField(null='True', to='control_measure.Bin', verbose_name='Выгружаемые контейнеры', blank='True'),
        ),
    ]
