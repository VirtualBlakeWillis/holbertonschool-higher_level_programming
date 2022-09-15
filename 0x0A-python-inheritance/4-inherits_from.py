#!/usr/bin/python3
""" is a subclass """


def inherits_from(obj, a_class):
    """ another desc """
    return issubclass(type(obj), a_class) and type(obj) != a_class
