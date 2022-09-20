#!/usr/bin/python3
""" open a file, and print it out!
"""


def read_file(filename=""):
    """ logic
    """
    with open("filename", "r", encoding="utf=8") as f:
        for line in f:
            print(line, end='')
