#!/usr/bin/python3
"""
    0-read_file Module
"""


def read_file(filename=""):
    """
        reads a text file and prints to stdout

        Args:
            filename: name of file to be read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
