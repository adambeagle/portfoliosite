# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=32, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
