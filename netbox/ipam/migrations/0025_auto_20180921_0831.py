# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0024_auto_20180914_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrf',
            name='rd',
            field=models.CharField(max_length=21, verbose_name='Route distinguisher'),
        ),
    ]
