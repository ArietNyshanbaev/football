# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbb\xd0\xb8\xd0\xb3\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u041b\u0438\u0433\u0430',
                'verbose_name_plural': '\u041b\u0438\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('body', models.TextField(verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xbe')),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('readed', models.IntegerField(default=0, verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xbe\xd0\xb2')),
                ('added_by', models.ForeignKey(verbose_name=b'\xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbe \xd0\xba\xd0\xb5\xd0\xbc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u044c',
                'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b')),
                ('image_emblem', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xbe\xd0\xba \xd0\xba\xd0\xbb\xd1\x83\xd0\xb1\xd0\xb0', blank=True)),
                ('image_squad', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x81\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2', blank=True)),
                ('league', models.ForeignKey(verbose_name=b'\xd0\xbb\xd0\xb8\xd0\xb3\xd0\xb0', to='news.League')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u0430\u043d\u0434\u0430',
                'verbose_name_plural': '\u041a\u043e\u043c\u0430\u043d\u0434\u044b',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='team',
            field=models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0', to='news.Team'),
        ),
    ]
