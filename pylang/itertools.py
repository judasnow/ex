#!/usr/bin/env python


from itertools import *

q = chain('ABC', 'DEF', 'qqq')

q = dropwhile(lambda x: x<5, [1,4,6,4,1])

q = izip('ABCD', 'xy')

for x in q:
    print x