#!/usr/bin/python3
"""class with tojson method"""


class Student:
    """class student with tojson method"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json method"""
        json_result = {}
        for key, value in self.__dict__.items():
            json_result[key] = value
        return json_result
