# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-06 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20180205_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='addresses',
            field=models.ManyToManyField(blank=True, to='contacts.Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='emails',
            field=models.ManyToManyField(blank=True, to='contacts.Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phones',
            field=models.ManyToManyField(blank=True, to='contacts.Phone'),
        ),
    ]
