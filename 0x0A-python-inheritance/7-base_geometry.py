#!/usr/bin/python3
"""
    7-base_geometry Module
"""


class BaseGeometry:
    """
        Base Geometry class
    """

    def area(self):
        """
            Area function(not implemented)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates value

            Args:
                name: a string
                value: data type to be validated

            Raises:
                TypeError: when value is not an integer
                ValueError: when value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
