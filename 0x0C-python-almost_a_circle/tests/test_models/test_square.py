#!/usr/bin/python3
"""
    tests for the square class
"""
import unittest
from models import square
import inspect
import pep8
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """
        TestRectangleDocs class
    """

    def test_base_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_module_docs(self):
        self.assertTrue(len(square.__doc__) > 4)
        
    def test_class_docs(self):
        self.assertTrue(len(Square.__doc__) > 4)

    def test_method_docs(self):
        list_of_methods = inspect.getmembers(square.Square,
                                            inspect.isfunction)
        for methods in list_of_methods:
            method = Square.__name__ + '.' + methods[0]
            self.assertTrue(len(eval(method).__doc__) > 4)

class TestSquare(unittest.TestCase):
    """
        tests for all square methods
    """

    def test_square_id(self):
        """ test for the square id """
        s1 = Square(2)
        s2 = Square(2, 3, 4, 5)
        self.assertEqual(s1.id, 17)
        self.assertEqual(s2.id, 5)

    def test_size_setter(self):
        """ checks if the size is set properly """
        with self.assertRaises(TypeError):
            Square('2')
        with self.assertRaises(TypeError):
            Square((2, 2))

    def test_size_setter_for_neg(self):
        with self.assertRaises(ValueError):
            Square(-2)

    def test_square_area(self):
        """ checks for the area of square """
        s5 = Square(3)
        s6 = Square(100)

        self.assertEqual(s5.area(), 9)
        self.assertEqual(s6.area(), 10000)

    def test_square_str(self):
        """ checks for the string instance square """
        s5 = Square(3, 1, 3, 4)
        s6 = Square(100)

        self.assertEqual(str(s5), '[Square] (4) 1/3 - 3')
        self.assertEqual(str(s6), '[Square] (18) 0/0 - 100')

    def test_square_update(self):
        """ checks if the update method works well """
        s1 = Square(10)

        self.assertEqual(str(s1), '[Square] (19) 0/0 - 10')
        s1.update(5)
        self.assertEqual(str(s1), '[Square] (5) 0/0 - 10')
        s1.update(89, 100, 2, 3)
        self.assertEqual(str(s1), '[Square] (89) 2/3 - 100')

    def test_square_dictionary(self):
        """ checks if the square dictionary is valid """
        s1 = Square(10, 2, 1, 50)

        self.assertEqual(s1.to_dictionary(),
                        {'size': 10, 'id': 50, 'x': 2, 'y': 1})

    def check_if_dictionary(self):
        """ checks if to dictionary returns a dictionary """
        s1 = Square(10, 2, 1, 50)
        s1_dict = s1.to_dictionary()

        self.assertIs(type(s1_dict), dict)

