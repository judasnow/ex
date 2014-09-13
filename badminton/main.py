# coding=utf-8

import os
import sys
import logging

import tornado.web
import tornado.ioloop

logger = logging.getLogger("badminton")
logger.setLevel("DEBUG")


class MainHandler(tornado.web.RequestHandler):

    def prepend(self):
        logger.debug(self.request.body)

    def get(self):
        self.render("home.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler)
    ],
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path="badminton/tpl",
    DEBUG=True,
    autoreload=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


