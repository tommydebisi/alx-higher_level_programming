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
    iter = 0
    while iter < x:
        try:
            print(my_list[iter], end='')
            iter += 1
        except IndexError:
            break
    print()
    return iter
