# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0015_auto_20150626_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='measurement_error',
        ),
    ]
