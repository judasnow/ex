# coding=utf-8

def chain(*iters):
    """ 返回一个将所有参数链接起来的迭代器 """

    for iter in iters:
        for x in iter:
            yield x


