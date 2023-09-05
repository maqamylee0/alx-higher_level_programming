#!/usr/bin/python3
""" Peak integer finder """


def find_peak(list_of_integers):
    """ Find the peak integer of an un sorted list """
    l_list = list_of_integers
    l_list.sort()
    if l_list:
        return l_list[-1]
    else:
        return None
