#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Descor(object):

    def __get__(self, instance, owner):
        print "get:", instance, owner
        return hex(id(instance))

    def __set__(self, instance, value):
        print "set:", instance, value

    def __delete__(self, instance):
        print "del:", instance


class Data(object):
    def test(self):
        pass


class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage



