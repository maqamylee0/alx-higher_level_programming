#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i+j == 17:
            print("{}{}".format(i, j), end="\n")
        else:
            print("{}{}".format(i, j), end=", ")
