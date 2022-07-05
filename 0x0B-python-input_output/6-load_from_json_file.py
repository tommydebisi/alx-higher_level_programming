#!/usr/bin/python3
"""
    6-load_from_json_file Module
"""
import json as js


def load_from_json_file(filename):
    """
        decodes or deserializes a string representation
        and creates and object accordinly

        Args:
            filename: name of file to be used
    """
    with open(filename, encoding='utf-8') as file:
        deserial = js.load(file)   # serializes object into file

    return deserial
