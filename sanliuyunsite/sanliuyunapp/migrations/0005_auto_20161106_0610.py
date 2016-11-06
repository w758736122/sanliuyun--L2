# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanliuyunapp', '0004_article_font_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='font_size',
            field=models.IntegerField(choices=[(3, 3), (5, 5), (8, 8), (20, 20), (56, 56)], default=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=12, verbose_name='昵称'),
        ),
    ]
