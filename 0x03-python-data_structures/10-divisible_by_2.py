#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for i in my_list:
        if i % 2 == 0:
            list2[i] = True
        else:
            list2[i] = False
    return list2

