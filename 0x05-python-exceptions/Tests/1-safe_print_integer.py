#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with string format for integer

    Args:
        value: any data type

    Return:
        True if integer else false
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
