# coding=utf-8

from peewee import Model, MySQLDatabase

mysql_db = MySQLDatabase("d", user="root", password="$judasnow")

class ModelBase(Model):

    class Meta:
        database = mysql_db


