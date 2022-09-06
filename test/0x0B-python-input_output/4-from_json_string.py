#!/usr/bin/python3
"""A json to object function"""
import json


def from_json_string(my_str):
    """Return Python object representation of a json string"""
    return json.loads(my_str)
