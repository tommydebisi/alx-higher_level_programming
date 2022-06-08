#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: initial dictionary
        value: to be checked in dict to delete

    Return:
        updated dictionary or intial dictionary if value not found
    """
    if not a_dictionary:
        return a_dictionary

    for key in list(a_dictionary.keys()):
        if value == a_dictionary.get(key):
            a_dictionary.pop(key)
    return a_dictionary
