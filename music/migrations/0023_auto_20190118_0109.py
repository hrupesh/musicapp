# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-17 19:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0022_auto_20190117_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2019, 1, 18, 1, 9, 8, 827005)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2019, 1, 18, 1, 9, 22, 354296)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
