# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0010_auto_20150412_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_op',
        ),
    ]
