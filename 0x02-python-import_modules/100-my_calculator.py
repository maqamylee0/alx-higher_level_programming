#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys

if __name__ == "__main__":
    length = len(sys.argv)
    argv = sys.argv

    if (length - 1) != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        if argv[2] == '+':
            result = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == '-':
            result = sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == '*':
            result = mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        elif argv[2] == '/':
            result = div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
