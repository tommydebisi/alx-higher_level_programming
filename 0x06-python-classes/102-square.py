#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes

        Args:
            size: size of square
        """
        self.size = size

    def __eq__(self, other) -> bool:
        """
        Compares two objects instances if equal

        Args:
            other: other object instance
        """
        return self.area() == other.area()

    def __lt__(self, other) -> bool:
        """
        Compares two objects instances if one less than
        the other

        Args:
            other: other object instance
        """
        return self.area() < other.area()

    def __le__(self, other) -> bool:
        """
        Compares two objects instances if one less than equal
        to the other

        Args:
            other: other object instance
        """
        return self.area() <= other.area()

    def __ne__(self, other) -> bool:
        """
        Compares two objects instances if they're not equal

        Args:
            other: other object instance
        """
        return self.area() != other.area()

    def __gt__(self, other) -> bool:
        """
        Compares two objects instances if one is greater than
        the other

        Args:
            other: other object instance
        """
        return self.area() > other.area()

    def __ge__(self, other) -> bool:
        """
        Compares two objects instances if one is greater than
        or equal to the other

        Args:
            other: other object instance
        """
        return self.area() >= other.area()  # self.area() used to access method

    @property
    def size(self):
        """ Gets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes area of a square """
        return self.__size ** 2
