# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_measure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('event_date', models.DateField()),
                ('event_description', models.CharField(max_length=500)),
                ('event_bin', models.ForeignKey(to='control_measure.Bin')),
            ],
        ),
    ]
