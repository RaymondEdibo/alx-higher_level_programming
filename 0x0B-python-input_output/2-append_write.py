#!/usr/bin/python3
"""append string"""


def append_write(filename="", text=""):
    """appends file"""

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        return appendFile.write(text)
