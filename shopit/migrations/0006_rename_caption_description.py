# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-10 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopit', '0005_add_product_code_to_cart_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttranslation',
            old_name='caption',
            new_name='_caption',
        ),
        migrations.RenameField(
            model_name='producttranslation',
            old_name='description',
            new_name='_description',
        ),
    ]