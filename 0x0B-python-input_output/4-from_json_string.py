#!/usr/bin/python3
"""
    4-from_json_string Module
"""
import json as js


def from_json_string(my_str):
    """
        deserializes string format to python data
        structure

        Args:
            my_str: string to be deserialized

        Returns:
            object(Python data structure) represented by a
            JSON string
    """
    return js.loads(my_str)
