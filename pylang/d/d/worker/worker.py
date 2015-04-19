# -*- coding: utf-8 -*-

import re
import time
from functools import partial

from bs4 import BeautifulSoup
from tornado.httpclient import HTTPClient, HTTPError

from .base import WorkerBase


class DBGroupWorker(WorkerBase):

    def __init__(self, group_name):
        WorkerBase.__init__(self)

        self.imgs_dir_name = group_name
        self.list_page_url = "http://www.douban.com/group/%s/" % group_name


