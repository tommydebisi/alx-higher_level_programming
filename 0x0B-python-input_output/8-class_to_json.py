#!/usr/bin/python3
"""
    8-class_to_json Module
"""


def class_to_json(obj):
    """
        the dictionary description with simple data structure
        for JSON serialization of an object

        Args:
            obj: initial object
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    return {}
