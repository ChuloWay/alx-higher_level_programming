#!/usr/bin/python3
"""A file appending function"""


def append_write(filename="", text=""):
    """Appends a string to the end of file
    Args:
        filename (str): Name of the file to append to
        text (str): String to append to the file
    Returns:
        Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
