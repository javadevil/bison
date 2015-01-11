# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=512, verbose_name='First Name')),
                ('prefix', models.CharField(max_length=64, verbose_name='Prefix', blank=True)),
                ('is_company', models.BooleanField(verbose_name='Company', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
