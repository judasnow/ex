#!/usr/bin/env python

import logging
from functools import partial

def foo(x, y=2):
    print x
    print x + y
    
    
fw = partial(foo, y=2)
fw(4)


