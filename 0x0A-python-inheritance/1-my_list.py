#!/usr/bin/python3
"""class inheritance module"""


class MyList(list):
    """class extending a list and has an overides sorting method"""
    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
