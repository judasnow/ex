#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import multiprocessing

import tornado
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    print multiprocessing.cpu_count()

    #application.listen(8888)
    #loop = tornado.ioloop.IOLoop.instance()
    #loop.start()


