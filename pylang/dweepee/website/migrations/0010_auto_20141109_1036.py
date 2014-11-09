# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20141109_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(related_name='relationships', to='website.User')),
                ('to_user', models.ForeignKey(related_name='related_to', to='website.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to='website.User', through='website.Rela'),
            preserve_default=True,
        ),
    ]
