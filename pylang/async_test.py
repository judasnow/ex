# coding=utf-8

BUFFER_SIZE = 1024
item_count = 0

producer_gen = None
consumer_gen = None

def producer():
    while True:
        if item_count >= BUFFER_SIZE:
            consumer_gen.next()
        else:
            item_count = item_count + 1
            yield


def consumer():
    while True:
        if item_count <= 0:
            producer_gen.next()
        else:
            item_count = item_count - 1
            yield


def main():
    producer_gen = producer()
    consumer_gen = consumer()

    i = 0
    while True:
        i = i + 1
        if i >= 10000:
            print "item_count=%d" % item_count
            i = 0


if __name__ == "__main__":
    main()


