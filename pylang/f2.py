#!/usr/bin/env python
# coding=utf-8

class BaseHandler(object):
    
    def __init__(self):
        self.users = ("judasnow", "snow")


class HomeHandler(BaseHandler):
    
    def __init__(self):
        super(HomeHandler, self).__init__()
        
    def __call__(self, *args, **kwargs):
        for user in self.users:
            print user
        


if __name__ == "__main__":
    
    homeHandler = HomeHandler()
    homeHandler()
    
