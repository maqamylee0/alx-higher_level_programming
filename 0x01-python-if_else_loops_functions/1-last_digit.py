#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
n = number % 10
if n > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, n))
elif n == 0:
    print("Last digit of {} is {} and is 5".format(number, n))
else:
    print("Last digit of {} is {} and is less than 6 and not zero".format(number, n))
