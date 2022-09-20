#!/usr/bin/python3
""" write data to a file, return # of bytes written """


def write_file(filename="", text=""):
    """ logic """

    with open(filename, "w", encoding="utf-8") as f:
        x = f.write(text)

    return x
