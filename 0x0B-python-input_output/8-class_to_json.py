#!/usr/bin/python3
"""module convert serializable to json"""


def class_to_json(obj):
    """function converts objects to json via dicts"""
    json_result = {}
    for key, value in obj.__dict__.items():
        json_result[key] = value
    return json_result
