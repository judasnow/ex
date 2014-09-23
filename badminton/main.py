
import os
import sys

from badminton.lib.color_logging import logging

import tornado.web
import tornado.ioloop
import tornado.log

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)-15s | %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("badminton")
logger.setLevel("DEBUG")


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.logger = logger


class MainHandler(BaseHandler):

    def get(self):
        self.render("home.html")


class CircleHandler(BaseHandler):

    def get(self):
        self.write("cirles")


if __name__ == "__main__":

    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/circles", CircleHandler),
        (r"/events", EventsHandler),
        (r"/topics", TopicsHandler)
    ],

    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path="badminton/tpl",
    debug=True,
    autoreload=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


