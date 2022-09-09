#!/usr/bin/python3
"""
return a + b
"""


def add_integer(a, b=98):
    """ math and type checking """


    n1 = a
    n2 = b
    if type(a) is float:
        n1 = int(a)
    if type(b) is float:
        n2 = int(b)

    if type(n1) is not int:
        raise TypeError("a must be an integer")
    if type(n2) is not int:
        raise TypeError("b must be an integer")

    if a+1 == a:
        raise OverflowError("a too large")
    return (n1 + n2)
