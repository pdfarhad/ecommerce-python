# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-23 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
