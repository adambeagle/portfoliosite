# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150224_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=128, default=''),
            preserve_default=True,
        ),
    ]
