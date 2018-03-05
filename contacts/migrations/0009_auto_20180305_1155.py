# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-05 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_contact_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=models.ManyToManyField(related_name='contacts', to='contacts.Tag'),
        ),
    ]
