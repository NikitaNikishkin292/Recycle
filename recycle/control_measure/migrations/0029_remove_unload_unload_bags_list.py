# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0028_unload_unload_bags_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unload',
            name='unload_bags_list',
        ),
    ]
