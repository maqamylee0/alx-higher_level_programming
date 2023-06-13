#!/usr/bin/python3
"""add args to python list then to file then to json"""


import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def save_json_save_file(filename):
    """adds args to json file"""
    list_args = sys.argv[1:]
    if exists('add_item.json'):
        json_obj = load_from_json_file(filename)
    else:
        json_obj = []
    join_obj = [*json_obj, *list_args]
    save_to_json_file(join_obj, filename)


if __name__ == '__main__':
    save_json_save_file("add_item.json")
