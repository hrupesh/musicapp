# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-06 18:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181207_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]