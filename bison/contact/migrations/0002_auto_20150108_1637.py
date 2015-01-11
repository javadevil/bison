# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tel',
            fields=[
                ('addition_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='contact.Addition')),
                ('tel_type', models.CharField(max_length=128, verbose_name='Tel Type')),
                ('number', models.CharField(max_length=128, verbose_name='Number')),
            ],
            options={
            },
            bases=('contact.addition',),
        ),
        migrations.AddField(
            model_name='addition',
            name='contact',
            field=models.ForeignKey(to='contact.Contact'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='contact',
            name='prefix',
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Name'),
            preserve_default=True,
        ),
    ]
