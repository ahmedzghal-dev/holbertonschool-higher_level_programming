#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """"check if a and b are integers or floats"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be a integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be a integer')
    else:
        return int(a) + int(b)
