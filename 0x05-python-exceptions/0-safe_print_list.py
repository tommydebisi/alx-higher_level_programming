#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints elements of a list

    Args:
        my_list: intial list
        x:  Number of elements to print

    Return:
        number of elements to print
    """
    try:
        for iter in range(x):
            print(my_list[iter], end='')
        print()
        return iter + 1
    except IndexError:
        print()
        return iter
