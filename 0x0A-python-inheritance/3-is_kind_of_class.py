#!/usr/bin/python3
"""
    3-is_kind_of_class Module
"""


def is_kind_of_class(obj, a_class):
    """
        checks for the instance of a specified
        class

        Args:
            obj: initial object
            a_class: class to confirm with the object

        Returns:
            True if object is an instance of or inherited the class
            or False if not
    """
    return isinstance(obj, a_class)
