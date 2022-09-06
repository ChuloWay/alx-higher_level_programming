#!/usr/bin/python3
"""A file reading function"""


def read_file(filename=""):
    """Output contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
