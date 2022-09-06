#!/usr/bin/python3
"""Defines a function that lookup an object attribute"""


def lookup(obj):
    """Return a list of an object's available attributes"""
    return (dir(obj))
