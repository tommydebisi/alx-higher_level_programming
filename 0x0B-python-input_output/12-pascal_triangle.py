#!/usr/bin/python3
"""
    12-pascal_triangle Module
"""


def pascal_triangle(n):
    """
        a list of lists of integers representing
        the Pascal's triangle of n
    """

    if n <= 0:
        return []

    res_list = []
    sub_list = []
    for i in range(n):

        if i == 0:
            res_list.append([1])
            sub_list.append(1)
            continue

        checker = [0] + sub_list + [0]

        new_sub_list = []
        for i in range(len(checker)):
            if i + 1 != len(checker):
                new_sub_list.append(checker[i] + checker[i + 1])
        res_list.append(new_sub_list)
        sub_list = new_sub_list

    return res_list
