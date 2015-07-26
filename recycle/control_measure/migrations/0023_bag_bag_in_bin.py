# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0022_measurement_measurement_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='bag_in_bin',
            field=models.OneToOneField(null='True', blank='True', verbose_name='В контейнере', to='control_measure.Bin'),
        ),
    ]
