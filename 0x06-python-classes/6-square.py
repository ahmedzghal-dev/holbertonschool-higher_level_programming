#!/usr/bin/python3
"""square class with private attribute size"""


class Square:
    """square class with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """Class method to initialize the square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get class property size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size property with error checks"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """get class property position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position property with error checks"""
        for elem in value:
            if elem < 0:
                raise TypeError("position must be a tuple\
                        of 2 positive integers")
            else:
                self.__position = value

    def area(self):
        """calculates the area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character # and position:
        if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print()
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
