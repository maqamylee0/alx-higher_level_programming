#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv)
    argv = sys.argv
    sum = 0
    for i in range(length - 1):
        sum = sum + int(argv[i + 1])
    print("{}".format(sum))
