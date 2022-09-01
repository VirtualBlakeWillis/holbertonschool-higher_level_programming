#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if (number < 0):
    result = "negative"
if (number > 0):
    result = "positive"
if (number == 0):
    result = "zero"

print("{:d} is {:s}".format(number, result))
