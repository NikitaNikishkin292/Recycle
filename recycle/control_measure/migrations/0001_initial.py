# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('bin_id', models.IntegerField(default=1)),
                ('bin_adress', models.CharField(max_length=200)),
                ('bin_volume', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('measurement_date', models.DateField()),
                ('measurement_cells_inside', models.DecimalField(max_digits=3, decimal_places=1)),
                ('measurement_cells_maximum', models.DecimalField(max_digits=3, decimal_places=1)),
                ('measurement_bin', models.ForeignKey(to='control_measure.Bin')),
            ],
        ),
    ]
