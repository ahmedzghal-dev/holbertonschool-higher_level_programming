#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class
    that inherited  from specified class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if obj is an instance of a class that inherited from
        the specified class - True
        otherwise - False
    """
    if type(obj) != a_class:
        return True
    else:
        return False
