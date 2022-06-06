#!/usr/bin/python3*
"""Writing the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize object's attribute"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, Value):
        if type(Value) is not int:
            raise TypeError("width must be an integer")
        if Value <= 0:
            raise ValueError("width must be > 0")
        self.__width = Value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, Value):
        if type(Value) is not int:
            raise TypeError("height must be an integer")
        if Value <= 0:
            raise ValueError("height must be > 0")
        self.__height = Value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, Value):
        if type(Value) is not int:
            raise TypeError("x must be an integer")
        if Value < 0:
            raise ValueError("x must be >= 0")
        self.__x = Value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, Value):
        if type(Value) is not int:
            raise TypeError("y must be an integer")
        if Value < 0:
            raise ValueError("y must be >= 0")
        self.__y = Value

    def area(self):
        """area Method
        this method will calculate the rectangle object's area
        """
        return self.__width * self.__height

    def display(self):
        """print in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            print('#' * self.__width)

    def __str__(self):
        """the __str__ method """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'\
            f' - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Update Rectangle"""
        my_list = ["id", "width", "height", "x", "y"]
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, my_list[arg], args[arg])

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle"""
        my_dic = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return my_dic
