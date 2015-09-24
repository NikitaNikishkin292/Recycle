# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0041_demos_measurement_demos_measurement_bin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demos_message',
            name='demos_message_user',
            field=models.ForeignKey(to='control_measure.Demos', verbose_name='Пользователь'),
        ),
    ]
