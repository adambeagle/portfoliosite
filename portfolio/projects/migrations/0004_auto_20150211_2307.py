# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('projects', '0003_auto_20150211_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ForeignKey(default=None, to='core.Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.ForeignKey(to='core.Link', null=True, related_name='liveurl_project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='source_url',
            field=models.ForeignKey(to='core.Link', null=True, related_name='source_project'),
            preserve_default=True,
        ),
    ]
