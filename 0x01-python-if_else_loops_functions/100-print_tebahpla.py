#!/usr/bin/python3
for char in range(90, 64, -1):
    if char % 2 == 0:
        char += 32
    print(chr(char), end = "")

