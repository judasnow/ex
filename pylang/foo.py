#!/usr/bin/env python
<<<<<<< HEAD

import logging
from functools import partial

def foo(x, y=2):
    print x
    print x + y
    
    
fw = partial(foo, y=2)
fw(4)

=======
# coding=utf-8

def test_metaclass(name, bases, dict):
    print 'The Class Name is', name
    print 'The Class Bases are', bases
    print 'The dict has', len(dict), 'elems, the keys are', dict.keys()

    # str is not callable
    return "yellow"

class M(type):

    def __new__(cls, name, bases, attrs):
        newattrs = dict(attrs, action_list=attrs["action_cooldown"].keys())
        return super(M, cls).__new__(cls, name, bases, newattrs)    

class User(object):
 
    __metaclass__ = test_metaclass
    
    action_cooldown = {"att": 5,
                       "def": 10}
    
    def action(self, action):
        if action in self.action_list:
            print "%s cooldown is %s" % (action, self.action_cooldown[action])

#u = User()
#u.action("att")
>>>>>>> 35e28b6feed485293c128429e7c8d974d92c40aa

