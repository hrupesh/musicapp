# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-16 18:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0017_auto_20190116_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('qty', models.IntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 0, 12, 47, 173550)),
        ),
        migrations.AlterField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 0, 12, 47, 173550)),
        ),
    ]
