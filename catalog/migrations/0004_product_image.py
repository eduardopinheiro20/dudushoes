# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-07 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180401_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Image'),
        ),
    ]
