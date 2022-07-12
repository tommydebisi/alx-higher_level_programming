#!/usr/bin/python3
"""
    rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
            Initializing special method

            Args:
                width: breadth of rectangle
                height: length of rectangle
                x: integer to be used
                y: integer to be used
                id: number of object created
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
            string representation special method

            Returns:
                string representation of object
        """
        line = '[{}] ({}) {}/{} - {}/{}'
        idd, xx, yy, hi = self.id, self.__x, self.__y, self.__height
        wi = self.__width

        return line.format(self.__class__.__name__, idd, xx, yy, wi, hi)

    @property
    def width(self):
        """
            gets the custom width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            gets the custom height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            gets the custom x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            gets the custom y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            computes the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            print the rectangle to stdout
        """
        print("\n" * self.__y, end='')

        for i in range(self.__height):
            print(" " * self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
            updates the objects values

            Args:
                args: arguments to be passed
                kwargs: keyword arguments to be used
        """
        i = 0
        if len(args) != 0:
            for key in self.__dict__.keys():
                try:
                    self.__dict__[key] = args[i]
                    i += 1
                except IndexError:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        to_dic = dict()
        attr_names = ['id', 'width', 'height', 'x', 'y']
        i = 0
        for val in self.__dict__.values():
            to_dic[attr_names[i]] = val
            i += 1

        return to_dic
