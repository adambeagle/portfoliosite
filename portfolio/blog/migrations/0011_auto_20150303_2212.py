# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subtitle',
            field=models.CharField(max_length=128, null=True, blank=True, default=''),
        ),
    ]
