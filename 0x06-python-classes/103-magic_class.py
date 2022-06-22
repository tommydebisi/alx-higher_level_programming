#!/usr/bin/python3
""" MagicClass module """
import math


class MagicClass:
    """ Declares a class named MagicClass """

    def __init__(self, radius=0) -> None:
        """
        Intializes the instance variables

        Args:
            radius: radius of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ Computes area of a circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Computes circumference of a circle """
        return 2 * math.pi * self.__radius
