#!/usr/bin/python3
"""
    8-class_to_json Module
"""
import json as js


def class_to_json(obj):
    """
        the dictionary description with simple data structure
        for JSON serialization of an object

        Args:
            obj: initial object
    """
    settle = js.dumps(obj.__dict__)
    return js.loads(settle)
