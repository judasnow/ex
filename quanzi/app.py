# coding=utf-8

import markdown
import os.path
import re
import torndb
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata

from tornado.options import define, options
from tornado.concurrent import Future


define("port", default=6000, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="test", help="blog database name")
define("mysql_user", default="test", help="blog database user")
define("mysql_password", default="test", help="blog database password")


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", HomeHandler)
        ]
        settings = dict(
            website_title=u"Circle test",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("blogdemo_user")
        if not user_id: return None
        return self.db.get("SELECT * FROM authors WHERE id = %s", int(user_id))


class HomeHandler(BaseHandler):

    def post(self):
        fe = tornado.gen.maybe_future(2)

        files = self.request.files
        for key in files.keys():
            # key 也就是 input#file 指定的值 为什么会是一个 list
            # 难道是为了 html5 中的多文件上传？
            f = files[key][0]
            fp = open(f["filename"], "w")
            fp.write(f["body"])
            fp.close()

    def get(self):
        f = self.ff("http://www.baidu.com")
        print f.result()

    def ff(self, url):
        http_client = tornado.httpclient.AsyncHTTPClient()
        my_future = Future()
        fetch_future = http_client.fetch(url)
        fetch_future.add_done_callback(
            lambda f: my_future.set_result(f.result()))
        return my_future

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


