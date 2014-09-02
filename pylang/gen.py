# coding=utf-8

import time

from ya_itertools.count import count
from ya_itertools.cycle import cycle
from ya_itertools.repeat import repeat
from ya_itertools.chain import chain


def main():
    gen = chain("abc", "def", "ghi")
    for n in gen:
        print str(n)

if __name__ == "__main__":
    main()


