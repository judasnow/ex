#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


def qqq(a):
    """ in qqq """
    pass


def wa(func):

    @functools.wraps(qqq)
    def wrap(*args):
        return func()

    return wrap


@wa
def foo(x):
    print x


print foo.__name__



