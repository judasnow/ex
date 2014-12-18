#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User(object):

    def __init__(self, name):
        self.name = name

    def puser(self):
        print "name is :%s" % self.name


class Student(User):

    def __init__(self, name, sid):
        super(Student, self).__init__(name)
        self.sid = sid

    def puser(self):
        print "%s:%s" % (self.sid, self.name)


v = Student("v", "121")
v.puser()


