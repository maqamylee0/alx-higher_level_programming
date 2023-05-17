#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = [replace if i == search else search for i in my_list]
    return list2
