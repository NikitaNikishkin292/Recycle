# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0008_auto_20150620_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='type_short_name',
            field=models.CharField(null='True', max_length=20),
        ),
    ]
