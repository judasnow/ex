#!/usr/bin/env python
# coding=utf-8


# a Descriptors
class Desc(object):

    data = None

    def __get__(self, instance, owner):
        print instance
        print owner
        return "1024"
        
    def __set__(self, instance, value):
        print instance
        self.data = value
        
    def __delete__(self, instance):
        pass


class Foo(object):
    
    desc = Desc()
    
    def __init__(self):
        pass
        

f = Foo()
print f.desc