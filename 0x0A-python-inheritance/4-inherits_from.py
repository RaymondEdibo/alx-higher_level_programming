#!/usr/bin/python3
"""Function which inherits"""


def inherits_from(obj, a_class):
    """Function which inherits"""

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return isinstance(obj, a_class)
