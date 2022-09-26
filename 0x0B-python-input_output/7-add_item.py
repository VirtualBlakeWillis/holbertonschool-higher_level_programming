#!/usr/bin/python3
""" Script that adds all arguments to a Python list, then saves """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fn = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(fn)
except:
    pass

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, fn)
