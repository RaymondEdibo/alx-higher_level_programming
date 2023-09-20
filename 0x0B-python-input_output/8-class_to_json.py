#!/usr/bin/python3
"""return dictionary"""


def class_to_json(obj):
    """Returns JSON dictionary description"""

    return obj.__dict__
