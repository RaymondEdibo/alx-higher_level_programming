#!/usr/bin/python3
"""Base"""
import json


class Base:
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        work method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON standard
        """
        if list_dictionaries is [None, ""]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON representation writer
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".json", "w+") as my_file:
            my_file.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        """
        returns json_string
        """
        if json_string is [None, ""]:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns instance with all set attributes
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            tmp.update(**dictionary)
            return tmp
        if cls.__name__ == "Square":
            tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        returns list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to CSV
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".csv", "w+") as my_file:
            my_file.write(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        returns list of instances
        """
        try:
            with open(cls.__name__ + ".csv", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []
