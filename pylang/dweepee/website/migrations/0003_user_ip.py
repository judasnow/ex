# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip',
            field=models.CharField(default=b'', max_length=27),
            preserve_default=True,
        ),
    ]
