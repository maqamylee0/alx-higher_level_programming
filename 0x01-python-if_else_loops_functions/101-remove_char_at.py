#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str_copy = ""
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            str_copy += char
            i += 1
    return str_copy
