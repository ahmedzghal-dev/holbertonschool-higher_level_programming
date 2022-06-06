#!/usr/bin/python3
"""Base class"""


from os import path
import json
import csv


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiallize the object attribute"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string
        representation of list_objs to a file"""
        list = []
        if list_objs is not None:
            list = [items.to_dictionary() for items in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """json method that returns the list of the JSON string"""
        list = []
        if json_string is None or len(json_string) == 0:
            return list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """reurns a list of instances"""
        if path.exists(cls.__name__ + ".json") is False:
            return []
        with open(cls.__name__ + ".json", 'r') as file:
            list = cls.from_json_string(file.read())
            return [cls.create(**index) for index in list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method that saves data into a csv file"""
        new_csv_file = cls.__name__ + ".csv"
        with open(new_csv_file, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=headers)
                for objects in list_objs:
                    writer.writerow(objects.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads csv data"""
        new_csv_file = cls.__name__ + ".csv"
        try:
            with open(new_csv_file, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                my_dict = csv.DictReader(file, fieldnames=headers)
                my_dict = [dict([key, int(value)] for key, value in
                                f.items()) for f in my_dict]
                return [cls.create(**argument) for argument in my_dict]
        except FileNotFoundError:
            return []
