#!/usr/bin/python3
"""
    2-is_same_class Module
"""


def is_same_class(obj, a_class):
    """
        checks for the exact instance of a specified
        class

        Args:
            obj: initial object
            a_class: class to confirm with the object

        Returns:
            True if object is an exactly the instance of the class
            or False if not
    """
    if type(obj) is not a_class:
        return False
    return True
