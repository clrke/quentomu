# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0007_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='quentomu.Topic', default=None),
            preserve_default=False,
        ),
    ]
