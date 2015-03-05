# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20150211_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_url',
            field=models.ForeignKey(null=True, blank=True, to='core.Link', related_name='liveurl_project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_url',
            field=models.ForeignKey(null=True, blank=True, to='core.Link', related_name='source_project'),
        ),
    ]
