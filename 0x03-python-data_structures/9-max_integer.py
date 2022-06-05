#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list

    Args:
        my_list: list to check from

    Return:
        biggest integer of list or none if
        list is empty
    """
    if not my_list:
        return None

    highest = 0
    for i in range(len(my_list)):
        highest = my_list[i] if (my_list[i] > highest) else highest
    return highest
