#!/usr/bin/python3
"""module to append to file"""


def append_write(filename="", text=""):
    """function appends to file"""
    with open(filename, 'a') as file:
        appended = file.write(text)
        return appended
