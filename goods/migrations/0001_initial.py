# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ucenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('pid', models.ForeignKey(blank=True, to='goods.Dict', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gdescrption', models.CharField(max_length=200)),
                ('gunit', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=4, decimal_places=2)),
                ('gdetail', tinymce.models.HTMLField()),
                ('gpic', models.ImageField(upload_to=b'uploads')),
                ('dictID', models.ForeignKey(to='goods.Dict')),
            ],
        ),
        migrations.CreateModel(
            name='ViewInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipAddr', models.CharField(max_length=20)),
                ('goodID', models.ForeignKey(to='goods.GoodInfo')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='goodID',
            field=models.ForeignKey(to='goods.GoodInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userID',
            field=models.ForeignKey(to='ucenter.UserInfo'),
        ),
    ]
