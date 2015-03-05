# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(serialize=False, max_length=32, primary_key=True)),
                ('slug', models.SlugField()),
                ('type', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('technology', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('source', models.URLField(max_length=128)),
                ('live_url', models.URLField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
