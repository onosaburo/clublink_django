# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 07:44
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_teammember'),
        ('cms', '0002_auto_20170215_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('page'))),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cms.Page')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=64)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('sort', models.IntegerField(default=0)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cms.List')),
            ],
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('gallery')),
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([('club', 'slug')]),
        ),
    ]