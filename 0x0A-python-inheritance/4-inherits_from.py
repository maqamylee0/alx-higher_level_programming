#!/usr/bin/python3
"""checks if object is from inherited class"""


def inherits_from(obj, a_class):
    """function checks if object is from inherited class"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
