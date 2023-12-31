#!/usr/bin/python3
"""
adds two integers
Return: a+b integer
"""


def add_integer(a, b=98):
    """Function that validate the add of two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
