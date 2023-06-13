#!/usr/bin/python3
"""module write to file"""


def write_file(filename="", text=""):
    """overwrites existing file"""
    with open(filename, 'w', "utf-8") as file:
        writeen_chars = file.write(text)
        return writeen_chars
