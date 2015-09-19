# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0036_auto_20150912_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demos',
            name='demos_avatar',
            field=models.ImageField(upload_to='control_measure/avatars'),
        ),
    ]
