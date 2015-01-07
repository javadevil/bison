# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='f_name',
            field=models.CharField(max_length=256, verbose_name='First Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_company',
            field=models.BooleanField(default=False, verbose_name='Company'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='prefix',
            field=models.CharField(blank=True, max_length=64, verbose_name='Prefix'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='s_name',
            field=models.CharField(blank=True, max_length=256, verbose_name='Last Name'),
            preserve_default=True,
        ),
    ]
