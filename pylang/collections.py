#!/usr/bin/env python
#coding=utf-8

def foo(x):
    x["error"] = 123
    
    
na = {"ppp": 123}
foo(na)

print na