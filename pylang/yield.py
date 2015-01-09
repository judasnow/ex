#!/usr/bin/env python


def p():
    while True:
        print "p"
        yield c
    
def c():
    while True:
        print "c"
        yield p

p().next()
