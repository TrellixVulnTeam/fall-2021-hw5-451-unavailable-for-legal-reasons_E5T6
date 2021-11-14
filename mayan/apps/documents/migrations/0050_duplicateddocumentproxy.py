# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-22 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0049_auto_20181211_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuplicatedDocumentProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Duplicated document',
                'proxy': True,
                'verbose_name_plural': 'Duplicated documents',
                'indexes': [],
            },
            bases=('documents.document',),
        ),
    ]
