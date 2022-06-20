#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints the result

    Args:
        a:  integer
        b:  integer

    Return:
        value of the division otherwise none
    """
    result = None
    try:
        return (result := a / b)
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
