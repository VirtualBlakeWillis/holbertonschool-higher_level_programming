#!/usr/bin/python3
"""
return a + b
"""


def add_integer(a, b=98):
    """ math and type checking """

    n1 = int(a)
    n2 = int(b)

    if type(n1) is not int:
        raise TypeError("a must be an integer")
    if type(n2) is not int:
        raise TypeError("b must be an integer")

    return (n1 + n2)
