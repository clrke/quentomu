# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contact_number',
            field=models.CharField(default=None, max_length=20, blank=True),
            preserve_default=False,
        ),
    ]
