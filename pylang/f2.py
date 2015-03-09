#!/usr/bin/env python
# coding=utf-8


class BaseView(object):
    """统一的为 views handler 增加一些信息 比如统计信息等
    example:
    @BaseView
    def home(request, user_id):
        pass"""

    def __init__(self, handler):
        
        extra_info = {"username": "name"}
        
        def wrapper(*args, **kwargs):
            handler(extra_info=extra_info, *args, **kwargs)
        
        self.wrapper = wrapper

    def __call__(self, *args, **kwargs):
        self.wrapper(*args, **kwargs)


@BaseView
def homeView(request, *args, **kwargs):
    print kwargs


def main():
    homeView("request")


if __name__ == "__main__":
    main()

