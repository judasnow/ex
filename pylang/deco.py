# coding=utf-8


def struct(*args):

    class _Struct(type):
        def __new__(cls, name, bases, dcts):

            print "__new__ %s" % cls

            for key in args:
                setattr(cls, key, None)

            t = type(name, bases, dcts)
            return t

    return _Struct


class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        print "<{value}>".format(value=self.value)


class Add(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        print "<{left}*{right}>".format(left=self.left,
                                 right=self.right)


class Mul(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        print "<{left}+{right}>".format(left=self.left,
                                        right=self.right)

if __name__ == "__main__":
    print Number(2)


