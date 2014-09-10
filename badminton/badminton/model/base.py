# coding=utf-8

from peewee import Model, MySQLDatabase

mysql_db = MySQLDatabase("badminton",
                         host="127.0.0.1",
                         user="test",
                         passwd="test")

class Base(Model):

    class Meta:
        database = mysql_db


