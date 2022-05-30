#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


class BaseGeometry:
    """BaseGeomerty class"""
    def area(self):
        """raises an Exception with the message """
        raise Exception('area() is no implemented')

    def integer_validator(self, name, value):
        """validate if value is strictly positive integer grater than 0"""
        if isinstance(value, str):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
