# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0005_auto_20150411_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, related_name='receiver_id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, related_name='sender_id'),
            preserve_default=False,
        ),
    ]
