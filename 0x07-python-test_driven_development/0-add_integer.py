#!/usr/bin/python3
def add_integer(a, b=98):
    """ return a + b """
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

    return (n1 + n2)
