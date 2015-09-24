# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0039_demos_demos_bins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demos_Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('demos_message_date', models.DateField(verbose_name='Дата сообщения')),
                ('demos_message_content', models.CharField(verbose_name='Сообщение', max_length=500)),
                ('demos_message_status', models.IntegerField(choices=[(0, 'Измерение'), (1, 'Поздравление'), (2, 'Вывоз')], verbose_name='Тип сообщения')),
                ('demos_message_user', models.OneToOneField(to='control_measure.Demos', verbose_name='Пользователь')),
            ],
        ),
        migrations.AlterField(
            model_name='demos_measurement',
            name='demos_measurement_date',
            field=models.DateField(verbose_name='Дата замера'),
        ),
    ]
