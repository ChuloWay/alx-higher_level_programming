#!/usr/bin/python3
"""A Python class to json function"""


def class_to_json(obj):
    """Return json"""
    return obj.__dict__
