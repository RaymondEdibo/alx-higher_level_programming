#!/usr/bin/python3
""""load from json"""
import json


def load_from_json_file(filename):
    """Returns created object from JSON"""

    with open(filename, mode="r", encoding="UTF-8") as readFile:
        return json.load(readFile)
