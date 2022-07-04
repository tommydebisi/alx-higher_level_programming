#!/usr/bin/python3
"""
    10-square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square class
    """

    def __init__(self, size):
        """
            special method for initializing instance variables

            Args:
                size: size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # init parent with size
        self.__size = size
