# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-01 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='buy_nums',
            field=models.IntegerField(default=199, verbose_name='\u8d2d\u4e70\u4eba\u6570'),
        ),
        migrations.AddField(
            model_name='produce',
            name='prices',
            field=models.IntegerField(default=9.99, verbose_name='\u4ef7\u683c'),
        ),
    ]
