# coding=utf-8

import datetime

from peewee import TextField, DateTimeField, ForeignKeyField, CharField

from .base import ModelBase
from .topic import Topic


class Image(ModelBase):

    class Meta:
        pass

    topic = ForeignKeyField(Topic, related_name="images")
    origin_url = CharField(default="") 
    file_name = CharField(default="")
    file_class = CharField(default="")
    content = TextField(default="")
    caught_at = DateTimeField(default=datetime.datetime.now)


