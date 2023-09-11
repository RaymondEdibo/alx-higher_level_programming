#!/usr/bin/python3
""""True if object or false"""


def is_kind_of_class(obj, a_class):
    """checks if it returned true or false"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
