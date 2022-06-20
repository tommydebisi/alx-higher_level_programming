#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints x number of elements of a list and only integers

    Args:
        my_list: initial list
        x:  number of elements to access in list

    Return:
        number of integers printed
    """
    res = 0
    for iter in range(x):
        try:
            print("{:d}".format(my_list[iter]), end='')
            res += 1
        except (TypeError, ValueError):
            pass
    print()
    return res
