#!/usr/bin/python3
""" Rectangle module that defines rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ return Area of Rectangle """
        return self.width * self.height

    def display(self):
        """ visual representation of object """
        print("\n" * self.y, end='')
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ string representation of Rectangle """
        rep = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        rep += " - {}/{}".format(self.width, self.height)
        return rep

    def update(self, *args, **kwargs):
        """ Update values of Rectangle """
        attr = ["width", "height", "x", "y"]
        my_list = list(args)

        for k,v in kwargs.items():
            setattr(self, k, v)

        for i in range(len(my_list)):
            if i is 0:
                super().__init__(my_list[i])
            setattr(self, attr[i - 1], my_list[i])

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.int_validator(width, "width")
        self.__width = width

    @height.setter
    def height(self, height):
        self.int_validator(height, "height")
        self.__height = height

    @x.setter
    def x(self, x):
        self.int_validator(x, "x")
        self.__x = x

    @y.setter
    def y(self, y):
        self.int_validator(y, "y")
        self.__y = y