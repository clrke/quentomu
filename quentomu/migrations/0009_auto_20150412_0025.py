# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quentomu', '0008_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, to='quentomu.Post', null=True),
        ),
    ]
