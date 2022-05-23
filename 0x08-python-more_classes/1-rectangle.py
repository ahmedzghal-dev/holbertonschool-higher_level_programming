#!/usr/bin/python3
"""Square Class
This is a square
"""


class Rectangle:
    """Square Class
    Square with size
    """
    def __init__(self, width=0, height=0):
        """__init__
        initializing square
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """defines a rectangle by width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be a interger')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """defines a rectangle by height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be a interger')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
