# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141031_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_edited',
            field=models.DateTimeField(default=datetime.date(2014, 11, 4), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='posted',
            field=models.DateTimeField(default=datetime.date(2014, 11, 4), auto_now_add=True),
            preserve_default=False,
        ),
    ]
