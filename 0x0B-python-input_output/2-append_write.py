#!/usr/bin/python3
""" append text to a file, return # of bytes added """


def append_write(filename="", text=""):
    """ logic """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
