# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 00:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=datetime.datetime(2017, 5, 31, 0, 56, 33, 855000, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
    ]