# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbnail',
            new_name='thumbnail_image',
        ),
    ]