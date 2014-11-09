# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_user_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='from_user',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
        migrations.AddField(
            model_name='user',
            name='related_from',
            field=models.ManyToManyField(related_name='related_from_rel_+', to='website.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='related_to',
            field=models.ManyToManyField(related_name='related_to_rel_+', to='website.User'),
            preserve_default=True,
        ),
    ]
