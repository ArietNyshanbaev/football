# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20150507_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='note2',
            field=models.TextField(blank=True, null=True, verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbe\xd1\x80\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x82\xd1\x8b_x'),
        ),
        migrations.AlterField(
            model_name='field',
            name='note3',
            field=models.TextField(blank=True, null=True, verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbe\xd1\x80\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb0\xd1\x82\xd1\x8b_y'),
        ),
    ]