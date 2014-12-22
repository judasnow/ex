#!/usr/bin/env python
# coding=utf-8

def test_metaclass(name, bases, dict):
    print 'The Class Name is', name
    print 'The Class Bases are', bases
    print 'The dict has', len(dict), 'elems, the keys are', dict.keys()

    # str is not callable
    return "yellow"

    
def init_attributes(name, bases, dict):
    if 'attributes' in dict:
        for attr in dict['attributes']:
            dict[attr] = None

    return type(name, bases, dict)
    
class MetaSingleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
        return cls.instance

class M(type):

    def __new__(cls, name, bases, attrs):
        newattrs = dict(attrs, action_list=attrs["action_cooldown"].keys())
        return super(M, cls).__new__(cls, name, bases, newattrs)    


class User(object):
 
    __metaclass__ = MetaSingleton
    
    action_cooldown = {"att": 5,
                       "def": 10}
    
    def action(self, action):
        if action in self.action_list:
            print "%s cooldown is %s" % (action, self.action_cooldown[action])

u = User()
#u.action("att")

