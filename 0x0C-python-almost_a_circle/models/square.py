#!/usr/bin/python3
""" Square module that defines the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        rep = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        rep += " - {}".format(self.width)
        return rep

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.int_validator(value, "width")
        self.width = value
        self.height = value
