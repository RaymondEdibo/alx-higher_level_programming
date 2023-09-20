#!/usr/bin/python3
"""write file on UTF-8"""


def write_file(filename="", text=""):
    """writes UTF-8"""

    with open(filename, mode='w', encoding='utf-8') as write_File:
        return write_File.write(text)
