
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

    def flash(self, message, category="info"):
        if message == "":
            return
        else:
            self._flash_messages.append((category, message))

    def get_flashed_messages(self, with_categories=True, category_filter=[]):
        messages = self.get_secure_cookie("flash_messages")
        try:
            messages = tornado.escape.json_decode(messages) if messages else []
        except Exception as e:
            self.logger.error(e)
            messages = []

        self.clear_cookie("flash_messages")
        return messages

    def on_finish(self):
        self.set_secure_cookie("flash_messages",
                               tornado.escape.json_encode(self._flash_messages))

    def initialize(self):
        self.logger = logger
        self._flash_messages = []


class MainHandler(BaseHandler):

    def get(self):
        flash_messages = self.get_flashed_messages()
        self.write(flash_messages)

    def post(self):
        self.flash("foo", "form_error")
        self.flash("bar", "test")


class CircleHandler(BaseHandler):

    def get(self):
        self.write("cirles")


if __name__ == "__main__":

    app = tornado.web.Application([
        (r"/", MainHandler)
    ],

    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path="badminton/tpl",
    debug=True,
    cookie_secret="foobar",
    autoreload=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


