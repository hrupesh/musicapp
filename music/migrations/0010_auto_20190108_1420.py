# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-08 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_remove_album_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=2000, upload_to=''),
        ),
    ]
