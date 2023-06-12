#!/usr/bin/python3
"""list available attributes and methods"""


def lookup(obj):
    """function to list available atts and methods"""
    attr_methods = [i for i in dir(obj)]
    return attr_methods
