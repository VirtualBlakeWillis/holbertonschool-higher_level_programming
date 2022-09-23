#!/usr/bin/python3
""" Square module that defines the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """ Dictionary representation of Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """ Update values of Square """
        if args:
            my_list = list(args)
            attr = ["id", "width", "height", "x", "y"]
            myl = len(my_list)
            for i in range(len(my_list)):
                print(i)
                if i <= 1:
                    setattr(self, attr[i], my_list[i])
                else:
                    setattr(self, attr[i], my_list[i-1])

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.int_validator(value, "width")
        self.width = value
        self.height = value
