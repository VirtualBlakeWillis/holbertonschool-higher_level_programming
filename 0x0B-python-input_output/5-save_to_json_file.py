#!/usr/bin/python3
""" save obj to json """
import json


def save_to_json_file(my_obj, filename):
    """ logic """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
