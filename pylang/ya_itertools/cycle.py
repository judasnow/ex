# coding=utf-8

def cycle(p):

    i = 0
    p_len = len(p)

    while True:

        if i >= p_len:
            i = 1
        else:
            i = i + 1

        yield p[i-1]


