# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0018_measurement_measurement_mass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('bag_id', models.IntegerField(serialize=False, primary_key=True, verbose_name='Номер контейнера')),
                ('bag_status', models.IntegerField(default=2, choices=[(1, 'INSIDE_BIN'), (2, 'FULL_IN_WAREHOUSE'), (3, 'EMPTY_IN_WAREHOUSE')], verbose_name='Статус мешка')),
                ('bag_type', models.ManyToManyField(to='control_measure.Type')),
            ],
        ),
    ]
