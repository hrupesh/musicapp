# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-17 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0026_auto_20190118_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.ManyToManyField(to='music.Album'),
        ),
    ]