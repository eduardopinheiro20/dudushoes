# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-13 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(null=True, verbose_name='Tamanho'),
        ),
    ]
