#!/usr/bin/python3
"""
    3-to_json_string Module
"""
import json as js


def to_json_string(my_obj):
    """
        gets JSON representation of an object(string)

        Args:
            my_obj: initial object

        Returns:
            JSON representation of an object(string)
    """
    return js.dumps(my_obj)
