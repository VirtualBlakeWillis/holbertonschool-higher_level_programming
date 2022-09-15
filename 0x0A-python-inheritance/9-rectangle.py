#!/usr/bin/python3
""" Module for Rectangle class, subclass of BaseGeometry, with area and __str__
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        creat = "[Rectangle] "
        creat += str(self.__width)
        creat += "/"
        creat += str(self.__height)
        return creat
