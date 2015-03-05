# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150224_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-count']},
        ),
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
