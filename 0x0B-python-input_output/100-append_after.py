#!/usr/bin/python3
"""
    100-append_after Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to a file, after each line
        containing a specific string

        Args:
            filename: name of file to work on
            search_string: string to append after
            new_string: string to be appended
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        new_list = []
        for sentence in file:
            new_list.append(sentence)

            # check if search string is present in sentence
            if sentence.rfind(search_string) != -1:
                new_list.append(new_string)

        file.seek(0)    # move cursor to beginning
        file.write(''.join(new_list))
