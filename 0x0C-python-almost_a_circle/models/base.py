#!/usr/bin/python3
""" base module that defines base class """


class Base:
    """ private class variable """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise an object with id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def int_validator(self, value, name):
        """ integer validator method for subclass use """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")
        else:
            if value <= 0:
                raise ValueError(name + " must be > 0")
