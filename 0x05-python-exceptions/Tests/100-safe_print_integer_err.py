#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Function that prints an integer

    Args:
        value:  any type(integers, strings, etc)

    Return:
        True if value has been correctly printed
        else false
    """
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=stderr)
        return False
    except TypeError as ty:
        print("Exception: {}".format(ty), file=stderr)
        return False
