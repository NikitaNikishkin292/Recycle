# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0027_auto_20150805_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='bin_status',
            field=models.IntegerField(verbose_name='Статус контейнера', default=0, choices=[(1, 'Включен в вывоз'), (0, 'Не включен в вывоз')]),
        ),
    ]
