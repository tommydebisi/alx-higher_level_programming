#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    returns a list with all values multiplied by a number
    without using any loops.

    Args:
        my_list: intial list
        number: number to multiply elements with

    Return:
        list of multiplied elements by number
    """
    return list(map(lambda x: x * number, my_list))
