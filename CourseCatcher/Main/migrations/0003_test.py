# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20161211_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
