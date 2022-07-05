#!/usr/bin/python3
"""
    5-save_to_json_file Module
"""
import json as js


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file
        using JSON representation

        Args:
            my_obj: initial object
            filename: name of file to be used
    """
    with open(filename, 'w', encoding='utf-8') as file:
        js.dump(my_obj, file)   # serializes object into file
