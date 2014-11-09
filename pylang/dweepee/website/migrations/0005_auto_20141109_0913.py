# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20141109_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(to='website.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='message',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='user',
            name='related_from',
        ),
        migrations.RemoveField(
            model_name='user',
            name='related_to',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='membership',
            name='inviter',
            field=models.ForeignKey(related_name='membership_invites', to='website.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='website.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='website.Person', through='website.Membership'),
            preserve_default=True,
        ),
    ]
