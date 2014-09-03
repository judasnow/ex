# coding=utf-8

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

    _BUFFER_SIZE = 1024
    _item_count = 0

    _producer_gen = None
    _consumer_gen = None

    def _producer(self):
        while True:
            if self._item_count < self._BUFFER_SIZE:
                self._item_count = self._item_count + 1

            # 在整个过程中 
            yield self._consumer_gen.next()

    def _consumer(self):
        while True:
            if self._item_count > 0:
                self._item_count = self._item_count - 1

            yield self._producer_gen.next()

    def __init__(self):
        self._producer_gen = self._producer()
        self._consumer_gen = self._consumer()

    def run(self):
        self._producer_gen.next()

if __name__ == "__main__":
    pc = Pc()
    pc.run()


