#!/usr/bin/python3
""" JSON to class instance creation """
import json


def load_from_json_file(filename):
    """ logic """

    with open(filename, "r") as file:
        x = json.loads(file.read())
        return x
