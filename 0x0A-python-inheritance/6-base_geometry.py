#!/usr/bin/python3
"""class with public method"""


class BaseGeometry:
    """base geo class based on 5base geo with public method"""
    def area(self):
        raise Exception("area() is not implemented")
