# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150224_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(max_length=32),
        ),
    ]
