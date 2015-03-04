#!/usr/bin/env python

<<<<<<< HEAD
class Foo(object):
    pass
    
    
class Bar(Foo):
    def __init__(self):
        print super(Bar, self)


b = Bar()
=======
import logging
from functools import partial

def foo(x, y=2):
    print x
    print x + y
    
    
fw = partial(foo, y=2)
fw(4)

=======
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
    
<<<<<<< HEAD
    def __init__(self):
        pass
        
=======
    def action(self, action):
        if action in self.action_list:
            print "%s cooldown is %s" % (action, self.action_cooldown[action])

#u = User()
#u.action("att")
>>>>>>> 35e28b6feed485293c128429e7c8d974d92c40aa
>>>>>>> a32daadd120eb9933760be618b6a018dcde1a414

f = Foo()
print f.desc
>>>>>>> ac42c10c57090b0b584ad652e192f9f06ccb3b02
