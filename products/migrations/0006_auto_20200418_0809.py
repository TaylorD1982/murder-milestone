# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200416_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='product',
            name='street',
        ),
        migrations.RemoveField(
            model_name='product',
            name='town',
        ),
    ]