# coding=utf-8

def count(start=0, step=1):
    """
    @args
    start, [step]

    @results
    start, start+step, start+2*step, ...

    @exps
    count(10) --> 10 11 12 13 14 ....
    """
    i = 0
    while True:
        i = i + 1
        yield start + (i * step)


