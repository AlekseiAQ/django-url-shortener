# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appurl',
            name='shortcode',
            field=models.CharField(default='appdefaultshortcode', max_length=15),
            preserve_default=False,
        ),
    ]
