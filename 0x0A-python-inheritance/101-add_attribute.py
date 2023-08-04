#!/usr/bin/python3
"""module to add attr to object if possible"""


def add_attribute(obj, name, value):
    """ adds attribute to obj if possible"""
    if hasattr(type(obj), '__dict__') and name in type(obj).__dict__:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
