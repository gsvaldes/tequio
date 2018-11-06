# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-06 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='contacts.Contact')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]