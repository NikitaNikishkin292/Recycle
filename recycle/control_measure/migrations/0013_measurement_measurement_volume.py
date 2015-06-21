# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0012_auto_20150621_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='measurement_volume',
            field=models.IntegerField(verbose_name='Объём', blank='True', null='True'),
        ),
    ]
