#!/usr/bin/python3
"""
return a + b
"""


def add_integer(a, b=98):
    """ math and type checking """
    type_a = type(a)
    type_b = type(b)
    if type_a is not int and type_a is not float:
        raise TypeError("a must be an integer")
    
    if type_b is not int and type_b is not float:
        TypeError("b must be an integer")
    
    n1 = int(a)
    n2 = int(b)
    return (n1 + n2)
