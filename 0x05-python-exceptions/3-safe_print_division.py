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
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
