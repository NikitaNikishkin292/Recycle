# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0005_auto_20150618_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='bin_type',
            field=models.ForeignKey(null='True', to='control_measure.Type'),
        ),
    ]
