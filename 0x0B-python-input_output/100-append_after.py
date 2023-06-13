#!/usr/bin/python3
"""module adds new string if certain srting is found """


def append_after(filename="", search_string="", new_string=""):
    """func adds new string if certain stringis found"""
    with open(filename, 'r+', encoding='utf-8') as file:
        read_lines = file.readlines()
        file.seek(0)
        for i in read_lines:
            file.write(i)
            if search_string in i:
                file.write(new_string + '\n')
