#!/usr/bin/python3
"""Rectangle Class
This is a rectangle
"""


class Rectangle:
    """Rectangle Class
    rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """__init__
        initializing rectangle
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

    def area(self):
        """calculates the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """__str__ method
        this method will print the rectangle on print() or str()
        """
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return my_str
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += '#'
            if i is not (self.__height - 1):
                my_str += "\n"
        return my_str

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """
        strWidth = str(self.width)
        strHeight = str(self.height)
        return f"Rectangle({strWidth}, {strHeight})"
