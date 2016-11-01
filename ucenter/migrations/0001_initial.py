# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addrname', models.CharField(max_length=20)),
                ('addrdetail', models.CharField(max_length=200)),
                ('addrcode', models.IntegerField()),
                ('addrtel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('detail', models.TextField(max_length=1000)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('delivery', models.DecimalField(max_digits=4, decimal_places=0)),
                ('orderSum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('address', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('utel', models.IntegerField()),
                ('uaddress', models.CharField(max_length=200)),
                ('ucreatetime', models.DateTimeField()),
                ('loginID', models.OneToOneField(to='login.Login')),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='userID',
            field=models.ForeignKey(to='ucenter.UserInfo'),
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='loginID',
            field=models.OneToOneField(to='ucenter.UserInfo'),
        ),
    ]
