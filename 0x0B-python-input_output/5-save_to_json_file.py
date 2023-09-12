#!/usr/bin/python3
"""writes object to text"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text with JSON"""

    with open(filename, mode="w", encoding="utf-8") as saveFile:
        json.dump(my_obj, saveFile)
