# coding=utf-8

import tornado

from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase

class TestCircle(AsyncTestCase):

    @tornado.testing.gen_test
    def test_http_fetch(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://www.tornadoweb.org")
        self.assertIn("FriendFeed", response.body)


