# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0035_demos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demos',
            name='demos_sochnik_count',
            field=models.IntegerField(default=0, verbose_name='Сочников накполено'),
        ),
    ]
