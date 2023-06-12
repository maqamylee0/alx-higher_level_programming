#!/usr/bin/python3
"""class that inverts == and !=="""


class MyInt(int):
    """class that inverts == and !=="""
    def __eq__(self, other):
        """function that reverses- =="""
        return super().__ne__(other)
    def __ne__(self, other):
        """function to reverse !="""
        return super().__eq__(other)
