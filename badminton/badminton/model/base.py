# coding=utf-8

from peewee import (Model, MySQLDatabase, CharField, TextField, DateTimeField,
                    TimeField, IntegerField, BigIntegerField, BooleanField,
                    FloatField, DoubleField, DecimalField, PrimaryKeyField,
                    ForeignKeyField, DateField)

mysql_db = MySQLDatabase("badminton",
                         host="127.0.0.1",
                         user="test",
                         passwd="test")

class BaseModel(Model):

    class Meta:
        database = mysql_db


