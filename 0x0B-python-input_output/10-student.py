#!/usr/bin/python3
"""Student module.

Student class
"""


class Student():
    """Defines Student."""

    def __init__(self, first_name, last_name, age):
        """
        Student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation"""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
