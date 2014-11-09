# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20141109_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='from_user',
            new_name='to_user',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to='website.User'),
            preserve_default=True,
        ),
    ]
