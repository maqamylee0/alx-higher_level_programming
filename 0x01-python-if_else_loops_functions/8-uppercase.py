#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if (ord(char)) in range(0,96):
            new_str += (chr(ord(char)))
        else:
            new_str += chr(ord(char) - 32)
    print(f"{new_str}")
    return new_str

