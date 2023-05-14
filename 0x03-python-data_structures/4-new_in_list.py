#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list[:]
    if idx >= len(my_list) or idx < 0:
        return (my_list)
    else:
        list2[idx] = element
        return list2
