#!/usr/bin/env python
# coding=utf-8

""" 多线程访问数据库 
    修改同一条记录中的一项
"""

import threading
from peewee import *


db = MySQLDatabase(database="test", user="root",
                   password="root", host="192.168.1.113",
                   threadlocals=False)

class Record(Model):

    class Meta:
        db_table = "record"
        database = db

    record = IntegerField(default=0)

def add_record_1(record_id=1, times=10):
    with db.transaction():
        for i in range(0, times):
            record = Record.get(Record.id==record_id)
            record.record = record.record + 1
            print "%s => add record_id=%d %d to %d" % (threading.currentThread().name,
                                                       record_id, record.record, record.record + 1)
            record.save()

    db.close()

def main():
    record = Record.create()
    for i in range(0, 2):
        threading.Thread(target=add_record_1, name="T%d" % i, args=(record.id, 100)).start()


if __name__ == "__main__":
    main()


