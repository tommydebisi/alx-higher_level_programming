#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers in a list, in reverse order

    Args:
        my_list: list of integers
    """

    for integer in range((len(my_list) - 1), -1, -1):
        print("{:d}".format(my_list[integer]))
