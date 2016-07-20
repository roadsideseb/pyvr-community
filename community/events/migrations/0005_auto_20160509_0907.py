# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-08 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160314_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='total cost'),
        ),
    ]