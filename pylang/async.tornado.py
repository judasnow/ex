#!/usr/bin/env python
# coding=utf-8


from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)

    return response.body


def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        print returnesponse.body

    http_client.fetch(url, callback=handle_response)


def main():
    print asynchronous_fetch("http://www.baidu.com")


if __name__ == "__main__":
    main()

