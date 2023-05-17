#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    sum = 0
    for i in list_set:
        sum = sum + i
    return sum
