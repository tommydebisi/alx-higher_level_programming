def safe_print_list_integers(my_list=[], x=0):
    """
    Prints x number of elements of a list and only integers

    Args:
        my_list: initial list
        x:  number of elements to access in list

    Return:
        number of integers printed
    """
    try:
        res = 0
        for iter in range(x):
            if type(my_list[iter]) is not int:
                res -= 1
                continue
            print("{:d}".format(my_list[iter]), end='')
        print()
        return iter + res + 1
    except TypeError:
        print()
        return iter + res
