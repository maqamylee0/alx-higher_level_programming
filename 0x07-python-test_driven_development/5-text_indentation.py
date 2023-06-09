#!/usr/bin/python3
"""module to print lines after ?"""


def text_indentation(text):
    """function to take text and add new lines at points"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char.strip(), end='')
        if char in ('.', '?', ':'):
            print('\n' * 2, end='')
    print()
