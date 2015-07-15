# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0019_bag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='bag_id',
            field=models.IntegerField(primary_key=True, verbose_name='Номер мешка', serialize=False),
        ),
        migrations.AlterField(
            model_name='bag',
            name='bag_status',
            field=models.IntegerField(verbose_name='Статус мешка', default=2, choices=[(1, 'В контейнере'), (2, 'На складе полный'), (3, 'На складе пустой')]),
        ),
        migrations.AlterField(
            model_name='bag',
            name='bag_type',
            field=models.ManyToManyField(verbose_name='Тип контейнера', to='control_measure.Type'),
        ),
    ]
