#!/usr/bin/env python
# -*- coding: utf-8 -*-


def partial(func, *args, **keywords):
    
    def newfunc(*fargs, **fkeywords):
        
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)

    #newfunc.func = func
    #newfunc.args = args
    #newfunc.keywords = keywords

    return newfunc


def foo(x, y, z):
    return x + y + z
    

f = partial(foo, 1, 2);
print f(3)

class descor(object):

    def __get__(self, obj, item):
        return 2

    def __set__(self, obj, item, value):
        pass

class User(object):
    
    
    d = descor()
    
    def __init__(self):
        pass
            
    @property
    def name(self):
        pass
        
        
u = User()
print u.d



        

