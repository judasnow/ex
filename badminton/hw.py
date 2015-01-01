#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import multiprocessing

import tornado
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], autoreload=True)

    application.listen(8888)
    loop = tornado.ioloop.IOLoop.instance()
    loop.start()


