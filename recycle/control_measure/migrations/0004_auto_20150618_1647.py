# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0003_auto_20150605_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тип контейнера')),
                ('length', models.IntegerField(verbose_name='Длина', default=145)),
                ('width', models.IntegerField(verbose_name='Ширина', default=105)),
                ('heigth', models.IntegerField(verbose_name='Высота', default=165)),
            ],
        ),
        migrations.RemoveField(
            model_name='bin',
            name='bin_volume',
        ),
        migrations.AddField(
            model_name='measurement',
            name='measurement_percentage',
            field=models.IntegerField(verbose_name='Заполненность', default=50),
        ),
    ]
