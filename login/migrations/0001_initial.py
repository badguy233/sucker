# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lname', models.CharField(max_length=20)),
                ('lpassword', models.CharField(max_length=20)),
                ('lemail', models.CharField(max_length=50)),
            ],
        ),
    ]
