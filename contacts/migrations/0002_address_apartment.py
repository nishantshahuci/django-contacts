# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-13 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='apartment',
            field=models.CharField(max_length=10, null=True),
        ),
    ]