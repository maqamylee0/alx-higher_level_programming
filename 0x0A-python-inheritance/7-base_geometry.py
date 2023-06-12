#!/usr/bin/python3
"""class with public method"""


class BaseGeometry:
    """base geo class based on 5base geo with public method"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if isinstance(value, str):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
