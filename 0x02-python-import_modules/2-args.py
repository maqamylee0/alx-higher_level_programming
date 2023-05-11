#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)

    if length == 2:
        print("{} argument".format(length - 1))
    else:
        print("{} arguments".format(length - 1))

    for i in range(length - 1):
        print("{}: {}".format(i, argv[i + 1]))
