# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0003_auto_20150411_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver_id', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender_id', null=True),
        ),
    ]
