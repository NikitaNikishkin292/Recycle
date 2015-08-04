# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0025_unload'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='bin_status',
            field=models.BooleanField(verbose_name='Статус контейнера', default=False, choices=[(True, 'Включен в вывоз'), (False, 'Не включен в вывоз')]),
        ),
    ]
