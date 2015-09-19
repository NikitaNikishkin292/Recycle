# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0037_auto_20150919_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demos',
            name='demos_avatar',
            field=models.ImageField(upload_to='avatars'),
        ),
    ]
