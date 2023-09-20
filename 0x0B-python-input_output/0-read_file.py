#!/usr/bin/python3
"""read files UTF-8"""


def read_file(filename=""):
    """Read UTF-8"""

    with open(filename, mode='r', encoding='utf-8') as read_File:
        print(read_File.read(), end="")
