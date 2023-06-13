#!/usr/bin/python3
"""module to create obj from json file"""


import json


def load_from_json_file(filename):
    """load object from json file"""
    with open(filename) as file:
        return json.loads(file.read())
