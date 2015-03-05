# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('full_path', models.FilePathField(path='/home/adam/dev/portfoliosite/portfolio/static/images', recursive=True, max_length=128)),
                ('alt_text', models.CharField(null=True, max_length=64, blank=True)),
                ('caption', models.CharField(null=True, max_length=256, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('url', models.URLField()),
                ('text', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
