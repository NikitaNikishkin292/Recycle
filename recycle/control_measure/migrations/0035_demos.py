# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('control_measure', '0034_auto_20150912_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demos',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, parent_link=True, primary_key=True)),
                ('demos_sochnik_count', models.IntegerField(default=1, verbose_name='Сочников накполено')),
                ('demos_avatar', models.ImageField(upload_to='avatars')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
