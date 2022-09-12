#!/usr/bin/python3
""" prints a square with # """


def print_square(size):
    """ Error logic """

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float:
        new_size = int(size)
    new_size = int(size)
    if type(new_size) is not int:
        raise TypeError("size must be an integer")

    for row in range(new_size):
        for char in range(new_size):
            print("#", end="")
        print("")
