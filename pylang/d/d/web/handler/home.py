# coding=utf-8

import tornado

from .base import BaseHandler


__all__ = ["HomeHandler"]


class HomeHandler(BaseHandler):

    def get(self):
        self.render("home.html")


