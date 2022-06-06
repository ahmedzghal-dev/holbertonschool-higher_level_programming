#!/usr/bin/python3
"""Base class"""


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
