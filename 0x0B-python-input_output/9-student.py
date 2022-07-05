#!/usr/bin/python3
"""
    9-student Module
"""


class Student:
    """
        Student class
    """

    def __init__(self, first_name, last_name, age) -> None:
        """
            initialization special method

            Args:
                first_name: first name of student
                last_name: last name of student
                age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieves dictionary representation of Student
        """
        return self.__dict__.copy()
