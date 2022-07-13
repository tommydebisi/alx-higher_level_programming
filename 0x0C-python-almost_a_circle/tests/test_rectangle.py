#!/usr/bin/python3
"""
    tests for the rectangle class
"""
import unittest
from models import rectangle
import json
import inspect
import pep8
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """
        TestRectangleDocs class
    """

    def test_base_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_module_docs(self):
        self.assertTrue(len(rectangle.__doc__) > 4)
        
    def test_class_docs(self):
        self.assertTrue(len(Rectangle.__doc__) > 4)

    def test_method_docs(self):
        list_of_methods = inspect.getmembers(rectangle.Rectangle,
                                            inspect.isfunction)
        for methods in list_of_methods:
            method = Rectangle.__name__ + '.' + methods[0]
            self.assertTrue(len(eval(method).__doc__) > 4)

class TestRectangle(unittest.TestCase):
    """
        TestRectangleId class
    """

    def test_correct_id(self):
        r2 = Rectangle(12, 6, 1, 2, 12)
        self.assertEqual(r2.id, 12)

    def test_width_setter(self):
        with self.assertRaises(TypeError):
            Rectangle('3', 5)
        with self.assertRaises(TypeError):
            Rectangle(3.0, 5)

        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            Rectangle(-50, 5)

    def test_height_setter(self):
        with self.assertRaises(TypeError):
            Rectangle(3, '5')
        with self.assertRaises(TypeError):
            Rectangle(3, 5.0)
        with self.assertRaises(TypeError):
            Rectangle(4, [5, 7, 8])

        with self.assertRaises(ValueError):
            Rectangle(1, -5)

    def test_x_setter(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5, '3')
        with self.assertRaises(TypeError):
            Rectangle(3, 5, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(4, 7, [5, 7, 8])

        with self.assertRaises(ValueError):
            Rectangle(1, 5, -4)
        with self.assertRaises(ValueError):
            Rectangle(4, 50, -100)

    def test_y_setter(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 8, '3')
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 7, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(4, 7, 9, [5, 7, 8])

        with self.assertRaises(ValueError):
            Rectangle(1, 5, 2, -4)
        with self.assertRaises(ValueError):
            Rectangle(4, 50, 4, -100)

    def test_rect_area(self):
        r1 = Rectangle(3, 7)
        r2 = Rectangle(12, 6, 1, 2, 12)
        r3 = Rectangle(4, 5, 2, 3)

        self.assertEqual(r3.area(), 20)
        self.assertEqual(r2.area(), 72)
        self.assertEqual(r1.area(), 21)

    def test_str_method(self):
        """ Checks the str special method """

        r2 = Rectangle(12, 6, 1, 2, 12)
        r1 = Rectangle(3, 7)
        r3 = Rectangle(4, 5, 2, 3)

        self.assertEqual(str(r2), '[Rectangle] (12) 1/2 - 12/6')
        self.assertEqual(str(r1), '[Rectangle] (27) 0/0 - 3/7')
        self.assertEqual(str(r3), '[Rectangle] (28) 2/3 - 4/5')

    def test_rect_update_method_args(self):
        """ checks the rectangle update method """

        r4 = Rectangle(10, 10, 10, 10)

        r4.update(89, 2)
        self.assertEqual(str(r4), '[Rectangle] (89) 10/10 - 2/10')
        r4.update(89, 2, 3)
        self.assertEqual(str(r4), '[Rectangle] (89) 10/10 - 2/3')
        r4.update(89, 2, 3, 2, 1)
        self.assertEqual(str(r4), '[Rectangle] (89) 2/1 - 2/3')

    def test_rect_update_method_kwargs(self):
        """ checks the rectangle update method """

        r4 = Rectangle(10, 10, 10, 10)

        r4.update(width=89, id=2)
        self.assertEqual(str(r4), '[Rectangle] (2) 10/10 - 89/10')
        r4.update(id=89, height=2, width=3)
        self.assertEqual(str(r4), '[Rectangle] (89) 10/10 - 3/2')
        r4.update(x=89, y=2, id=3, width=2, height=1)
        self.assertEqual(str(r4), '[Rectangle] (3) 89/2 - 2/1')

    def test_rect_dictionary(self):
        """ checks if the square dictionary is correct """
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(13, 5, 6, 9, 10)

        self.assertEqual(r1.to_dictionary(),
                        {'id': 24, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        self.assertEqual(r2.to_dictionary(),
                        {'id': 10, 'width': 13, 'height': 5, 'x': 6, 'y': 9})

    def check_rect_if_dictionary(self):
        """ checks if to dictionary returns a dictionary """
        r1 = Rectangle(10, 2, 1, 50, 13)
        r_dict = r1.to_dictionary()

        self.assertIsInstance(type(r_dict), dict)
