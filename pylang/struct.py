#!/usr/bin/env python
# coding=utf-8

"""将一个 dict 转化成一个 object"""

from collections import namedtuple

MyStruct = namedtuple('MyStruct', 'a b d')
s = MyStruct(a=1, b={'c': 2}, d=['hi'])

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

        
def main():
    point = Struct(**{"foo": "bar"})
    print point.foo
    print s


if __name__ == "__main__":
    main()

