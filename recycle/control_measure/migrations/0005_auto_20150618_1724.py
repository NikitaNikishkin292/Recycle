# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0004_auto_20150618_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='heigth',
            new_name='type_heigth',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='length',
            new_name='type_length',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='type_name',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='width',
            new_name='type_width',
        ),
        migrations.AddField(
            model_name='type',
            name='type_description',
            field=models.CharField(max_length=100, verbose_name='Описание', default='bla bla bla'),
        ),
    ]
