# coding=utf-8

import datetime

from peewee import TextField, DateTimeField

from .base import ModelBase


class Topic(ModelBase):

    class Meta:
        pass

    origin_content = TextField()
    caught_at = DateTimeField(default=datetime.datetime.now)

Topic.create_table()
