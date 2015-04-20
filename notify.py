#!/usr/bin/env python

from abc import ABCMeta


class Subject(object):
    
    def __init__(self):
        self._observers = []
    
    def attach(self):
        pass
    
    def detach(self):
        pass
        
    def notify(self):
        pass

        
def main():
    pass
    

if __name__ == "__main__":
    main()

