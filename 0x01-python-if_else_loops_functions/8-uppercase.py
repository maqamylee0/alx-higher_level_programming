#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        new_str += (chr(ord(char) - 32))
    print(new_str)

