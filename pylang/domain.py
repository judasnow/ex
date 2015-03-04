#!/usr/bin/env python

_bar = 123

def f():
    _bar = 1024
    print _bar
    print id(_bar)

f()
print id(_bar)

