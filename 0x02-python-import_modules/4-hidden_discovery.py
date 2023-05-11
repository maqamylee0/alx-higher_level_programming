#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)
for i in names:
    if (i.startswith('__')):
        continue
    else:
        print(i)
