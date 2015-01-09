#!/usr/bin/env python


import time


def Yin():
    x = 0
    print "1024"
    while True:
        print "yin\n"
        time.sleep(1)
        x = yield x
        x += 1

    
if __name__ == "__main__":
    yin = Yin()
    print yin.next()
    print yin.send(20)
    print yin.close()
    #for _ in yin:
    #    print _

    
