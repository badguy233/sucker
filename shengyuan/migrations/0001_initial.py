# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goodID', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('userID', models.ForeignKey(to='ucenter.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
