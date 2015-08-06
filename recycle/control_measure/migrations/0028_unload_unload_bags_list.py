# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0027_auto_20150805_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='unload',
            name='unload_bags_list',
            field=models.ManyToManyField(blank='True', verbose_name='Необходимые мешки', to='control_measure.Bag'),
        ),
    ]
