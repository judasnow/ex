#!/usr/bin/env python


class Struct(type):

    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)
        
    def __init__(cls, name, bases, dct):
        super(Struct, cls).__init__(name, bases, dct)


class Number(object):
    __metaclass__ = Struct("value")
    
    
class Add(object):
    pass
    
    
class Multiply(object):
    pass
    
    
    
def main():
    pass
    
    
    
if __name__ == "__main__":
    main()
    
