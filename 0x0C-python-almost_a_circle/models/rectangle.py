#!/usr/bin/python3*


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

    """width public getter and setter"""
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

    """height public getter and setter"""
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

    """x public getter and setter"""
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

    """y public getter and setter"""
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

    """the area value of the Rectangle"""
    def area(self):
        return self.__width * self.__height

    """print in stdout the Rectangle instance with the character #"""
    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            print('#' * self.__width)

    """the __str__ method """
    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'\
            f' - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Update Rectangle
        """
        if args:
            for i in range(len(args)):
                if i == 0 and args[i] is not None:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if kwargs:
                for k, v in kwargs.items():
                    if k == "id" and v is not None:
                        self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

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
