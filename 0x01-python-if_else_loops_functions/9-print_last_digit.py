#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = (-number)
    n = number % 10
    print(n, end="")
    return n
