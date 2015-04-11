# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.CharField(max_length=160)),
                ('contact_number', models.CharField(null=True, max_length=20)),
                ('receiver', models.ForeignKey(related_name='receiver_id', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
