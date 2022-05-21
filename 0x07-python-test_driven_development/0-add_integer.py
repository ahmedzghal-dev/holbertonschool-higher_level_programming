#!/usr/bin/python3
"""function that adds two integers"""


def add_integer(a, b=98):
    """"function that adds two integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be a integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be a integer')
    else:
        return int(a) + int(b)
