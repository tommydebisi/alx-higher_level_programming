#!/usr/bin/python3
"""
    This script finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
        Gets the peak in the list
    """
    if not list_of_integers:
        return None

    start, end = 0, len(list_of_integers) - 1
    mid = start + (end - start) // 2

    while mid != start:
        left, right = list_of_integers[mid - 1], list_of_integers[mid + 1]

        if left < list_of_integers[mid] and right < list_of_integers[mid]:
            return list_of_integers[mid]

        # not a peak, check the highest btw left and right
        if left < right:
            start = mid
        else:
            end = mid

        mid = start + (end - start) // 2
    return list_of_integers[mid]
