#!/usr/bin/python3
""" JSON to class instance creation """
import json


def load_from_json_file(filename):

    with open(filename, "r") as file:
        x = json.loads(file.read())
        return x
