# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 01:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
    ]
