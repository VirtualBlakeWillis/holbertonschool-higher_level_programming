#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print("{:d}".format(number % 10))
        return
    print("{:d}".format((number * -1) % 10))
