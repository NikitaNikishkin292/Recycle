# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0033_demos_measurement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demos_measurement',
            old_name='demos_comment',
            new_name='demos_measurement_comment',
        ),
        migrations.RenameField(
            model_name='demos_measurement',
            old_name='demos_date',
            new_name='demos_measurement_date',
        ),
        migrations.RenameField(
            model_name='demos_measurement',
            old_name='demos_percentage',
            new_name='demos_measurement_percentage',
        ),
        migrations.RenameField(
            model_name='demos_measurement',
            old_name='demos_user',
            new_name='demos_measurement_user',
        ),
    ]
