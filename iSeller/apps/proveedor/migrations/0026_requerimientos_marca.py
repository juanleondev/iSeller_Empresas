# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0025_requerimientos'),
    ]

    operations = [
        migrations.AddField(
            model_name='requerimientos',
            name='marca',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
