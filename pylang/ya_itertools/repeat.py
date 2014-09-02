# coding=utf-8


def repeat(el, n):
    i = 0
    while True:
        if i <= n:
            i = i + 1
            yield el
        else:
            raise StopIteration()


