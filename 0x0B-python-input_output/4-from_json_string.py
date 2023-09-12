#!/usr/bin/python3
"""return JSON"""
import json


def from_json_string(my_str):
    """return python object"""

    return json.loads(my_str)
