# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d/img'),
        ),
    ]
