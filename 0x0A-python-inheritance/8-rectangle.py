#!/usr/bin/python3
"""class inheriting form basegeo"""


class Rectangle(BaseGeometry):
    """class inheriting from base geometry class"""
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
