#!/usr/bin/env python
# coding=utf-8

""" 多线程访问数据库 
    修改同一条记录中的一项
"""

import threading
from playhouse.pool import PooledMySQLDatabase
from peewee import *

db = PooledMySQLDatabase(
    "test",
    max_connections=32,
    stale_timeout=300,
    threadlocals=True,
    user="root",
    password="123456",
    host="127.0.0.1")


class Record(Model):
    class Meta:
        db_table = "record"
        database = db

    record = IntegerField(default=0)


class Record2(Model):
    class Meta:
        db_table = "record2"
        database = db

    record = IntegerField(default=0)


def add_record_1(record_id=1, record2_id=1, times=10):
        with db.transaction():
            for i in range(0, times):
                res = Record.raw("select * from record where id = '%d' FOR UPDATE" %
                                 record_id).execute()
                record = res.next()
                record.record = record.record + 1
                record.save()

                #Record.raw("update record set record = record+1 where id='%d'" % record_id).execute()
                #if i == 5:
                #    raise Exception("nop")
                #Record2.raw("update record2 set record = record+1 where id='%d'" % record2_id).execute()


def main():
    record = Record.create()
    record2 = Record2.create()

    for i in range(0, 16):
        threading.Thread(target=add_record_1, name="T%d" % i, args=(record.id, record2.id, 10)).start()


if __name__ == "__main__":
    main()


