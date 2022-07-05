#!/usr/bin/python3
"""
    101-add_attribute Module
"""


def add_attribute(obj, name, value):
    """
        create a class attribute

        Args:
            obj: initial object
            name: name of attributes
            value: value of attributes
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
