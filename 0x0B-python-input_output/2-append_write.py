#!/usr/bin/python3
"""
    2-append_write Module
"""


def append_write(filename="", text=""):
    """
        appends a string to a text file

        Args:
            filename: name of file to be written to
            text: string to be appended

        Returns:
            number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as file:
        written = file.write(text)

    return written
