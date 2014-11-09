# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20141109_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='website.User'),
            preserve_default=True,
        ),
    ]
