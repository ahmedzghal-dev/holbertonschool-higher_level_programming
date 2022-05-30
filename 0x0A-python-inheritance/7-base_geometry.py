#!/usr/bin/python3
class BaseGeometry:
    # Public instance method
    def area(self):
        raise Exception('area() is no implemented')

    def integer_validator(self, name, value):
        if isinstance(value, str):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
