#!/usr/bin/python3
""" prints a square with # """


def print_square(size):
    """ Error logic """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for char in range(size):
            print("#", end="")
        print("")
