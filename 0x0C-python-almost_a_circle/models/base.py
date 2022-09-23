#!/usr/bin/python3
""" base module that defines base class """
import json


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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes JSON string representation of list_objs to a file """
        my_list = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))
