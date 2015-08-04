# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0024_auto_20150804_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unload',
            fields=[
                ('unload_id', models.IntegerField(serialize=False, verbose_name='id выгрузки', primary_key=True)),
                ('unload_date', models.DateTimeField(verbose_name='Дата выгрузки')),
                ('unload_status', models.IntegerField(choices=[(0, 'Осуществленный'), (1, 'Запланированный')], verbose_name='Статус выгрузки', default=1)),
                ('unload_time_spent', models.IntegerField(null='True', verbose_name='Минут потрачено', blank='True')),
                ('unload_money_spent', models.IntegerField(null='True', verbose_name='израсходовано денег', blank='True')),
                ('unload_bins_list', models.ManyToManyField(to='control_measure.Bin', verbose_name='Выгружаемые контейнеры')),
            ],
        ),
    ]
