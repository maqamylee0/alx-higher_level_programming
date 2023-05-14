#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        c = (0, 0,)
    elif len(tuple_a) < 2:
        c = (0,)
    else:
        c = ()
    if len(tuple_b) < 1:
        d = (0, 0,)
    elif len(tuple_b) < 2:
        d = (0,)
    else:
        d = ()
    a = tuple_a[:2] + c
    b = tuple_b[:2] + d
    tup = tuple(sum(x) for x in zip(a, b))
    return tup
