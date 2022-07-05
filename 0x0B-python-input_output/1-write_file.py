#!/usr/bin/python3
"""
    1-write_file Module
"""


def write_file(filename="", text=""):
    """
        writes a string to a text file

        Args:
            filename: name of file to be written to
            text: string to written

        Returns:
            number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        written = file.write(text)

    return written  # number of characters written
