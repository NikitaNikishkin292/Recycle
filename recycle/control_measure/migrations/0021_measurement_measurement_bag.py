# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0020_auto_20150715_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='measurement_bag',
            field=models.IntegerField(null='True', verbose_name='Номер мешка', blank='True'),
        ),
    ]
