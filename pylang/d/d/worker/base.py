#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
from functools import partial

from bs4 import BeautifulSoup
from tornado.httpclient import HTTPClient, HTTPError

from d.models.topic import Topic
from d.models.image import Image

#from d.logging import logger


class WorkerBase(object):
    """ base worker """

    headers = {'User-Agent': 'Safari/537.36'}

    imgs_dir_name = ""
    list_page_url = ""
    topic_page_url_prefix = "http://www.douban.com/group/topic/"
    topic_link_re = re.compile("%s([0-9]{1,})/" % topic_page_url_prefix)

    def __init__(self):
        self.http_client = HTTPClient()
        self.fetch = partial(self.http_client.fetch, headers=self.headers)

    def fetch_list_page(self):
        return self.fetch(self.list_page_url)

    def parse_list_page(self, list_page_body):
        """ 解析页面中的链接 返回全部的 topic_id """

        soup = BeautifulSoup(list_page_body)

        # group-topics > tr
        group_topics = soup.find(id="group-topics")
        group_topics_links = group_topics.find_all("a")

        topic_ids = []
        for link in group_topics_links:
            # 过滤出话题链接
            reg = self.topic_link_re.match(link.get("href"))
            if reg:
                topic_ids.append(reg.group(1))

        return topic_ids

    def fetch_topic_page(self, topic_id):
        url = self.topic_page_url_prefix + str(topic_id)
        return self.fetch(url)

    def parse_topic_page(self, topic_page_body):

        soup = BeautifulSoup(topic_page_body)
        link_report = soup.find(id="link-report")
        imgs = link_report.findAll("img")

        img_srcs = []
        for img in imgs:
            img_srcs.append(img.get("src"))

        return img_srcs

    def fetch_img(self, img_url):
        return self.fetch(img_url)

    def start_flow(self):
        """ 执行一个完整的流程 """

        #logger.debug("%s start flow" % list_page_url)

        list_page_res = self.fetch_list_page()
        topic_ids = self.parse_list_page(list_page_res.body)

        # 遍历抓取每一个 topic 页面中的 img 元素

        for topic_id in topic_ids:
            try:

                try:
                    # 如果 topic 已经存在 就不再抓取
                    if Topic.get(id=topic_id):
                        continue
                except:
                    pass

                topic_page_res = self.fetch_topic_page(topic_id)
                topic = Topic.create(id=topic_id, origin_content=topic_page_res.body)

                img_urls = self.parse_topic_page(topic_page_res.body)

                imgs = []
                for img_url in img_urls:

                    try:
                        if Image.get(origin_url=img_url):
                            continue

                    except:
                        pass

                    img = self.fetch_img(img_url)

                    if not os.path.exists("imgs/%s" % self.imgs_dir_name):
                        os.mkdir("imgs/%s" % self.imgs_dir_name)

                    file_name = "imgs/%s/%s.jpg" % (self.imgs_dir_name, time.time())

                    Image.create(origin_url=img_url, file_name=file_name, topic=topic)

                    fp = open(file_name, "w+")
                    fp.write(img.body)
                    fp.close()

            except Exception as e:
                print e

        self.http_client.close()



