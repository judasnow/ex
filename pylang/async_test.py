# coding=utf-8

from time import sleep

class Pc(object):
    """
     loop
           while q is not full
               create some new items
               add the items to q
           yield to consume

     loop
           while q is not empty
               remove some items from q
               use the items
           yield to produce
    """

    _BUFFER_SIZE = 10
    _item_count = 0

    _producer_gen = None
    _consumer_gen = None

    def _producer(self):
        # 为了不让函数退出 
        # 因为函数退出 就没有意义了
        while True:
            if self._item_count < self._BUFFER_SIZE:
                self._item_count = self._item_count + 1

            # 在整个过程中 关键的一点就是 yield 之后的表达式 是可以返回
            # 的 因此就有了 callee 和 协程之间的 通信渠道 
            #（另一条是 使用全局变量）
            sleep(2)
            print "will yield to consumer, and _item_count={0}".format(self._item_count)
            yield self._consumer_gen

    def _consumer(self):
        while True:
            if self._item_count > 0:
                self._item_count = self._item_count - 1

            sleep(2)
            print "will yield to producer, and _item_count={0}".format(self._item_count)
            yield self._producer_gen

    def __init__(self):
        # 生成相应的生成器
        self._producer_gen = self._producer()
        self._consumer_gen = self._consumer()

    def run(self):
        gen = self._producer_gen
        while True:
            gen = gen.next()

if __name__ == "__main__":
    pc = Pc()
    pc.run()


