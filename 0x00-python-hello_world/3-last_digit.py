#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
printStr = "Last digit of {:d} is {:d} and is {:s}"
if number < 0:
    lastDigit = ((number * -1) % 10) * -1
else:
    lastDigit = number % 10

if lastDigit > 5:
    response = "greater than 5"
elif lastDigit == 0:
    response = "0"
else:
    response = "less than 6 and not 0"

print(printStr.format(number, lastDigit, response))
