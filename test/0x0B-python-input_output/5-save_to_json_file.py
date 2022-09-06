#!/usr/bin/python3
"""A json file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write json representation of object to file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
