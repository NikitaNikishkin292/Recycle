# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0029_remove_unload_unload_bags_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='City_Pace',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('city_pace_date', models.DateField(verbose_name='Дата')),
                ('city_pace_value', models.DecimalField(max_digits=4, verbose_name='Темп м3/сутки', decimal_places=1)),
            ],
        ),
    ]
