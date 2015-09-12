# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_measure', '0032_auto_20150808_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demos_Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demos_date', models.DateTimeField(verbose_name='Дата замера')),
                ('demos_percentage', models.DecimalField(default=50, decimal_places=1, max_digits=4, verbose_name='Процент')),
                ('demos_comment', models.CharField(max_length=1000)),
                ('demos_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
