#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    num = -num
n = num % 10
if number < 0:
    n = -n
if n > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, n))
elif n == 0:
    print("Last digit of {} is {} and is 0".format(number, n))
else:
    print(f"Last digit of {number} is {n} and is less than 6 and not zero")
