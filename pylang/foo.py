#!/usr/bin/env python

class Foo(object):
    pass
    
    
class Bar(Foo):
    def __init__(self):
        print super(Bar, self)


b = Bar()