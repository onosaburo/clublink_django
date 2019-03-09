# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 06:26
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0012_auto_20170222_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='clubs.Club'),
        ),
    ]