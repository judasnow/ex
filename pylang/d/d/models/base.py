# coding=utf-8

from peewee import Model, MySQLDatabase
from d.config import db

mysql_db = MySQLDatabase(db["name"],
                         user=db["user"],
                         password=db["pwd"])

class ModelBase(Model):

    class Meta:
        database = mysql_db


