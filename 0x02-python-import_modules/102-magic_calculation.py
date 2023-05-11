#!/usr/bin/python3
tup = ('add', 'sub')
import magic_calculation_102
add = magic_calculation_102.add
sub = magic_calculation_102.sub
if a < b:
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c
else:
    return sub(a, b)
