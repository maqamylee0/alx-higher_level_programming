#!/usr/bin/python3
"""module reads file"""


def read_file(filename=""):
    """function reads file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
