#!/usr/bin/python3
"""
    tests for the rectangle class
"""
import unittest
from models import rectangle
import json
import inspect
import pep8
import os
from unittest.mock import patch
from io import StringIO
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

    def test_when_required_args_not_passed(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(12)

    def test_width_setter_for_type(self):
        with self.assertRaises(TypeError):
            Rectangle('3', 5)
        with self.assertRaises(TypeError):
            Rectangle(3.0, 5)

    def test_width_setter_for_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            Rectangle(-50, 5)

    def test_height_setter_for_type(self):
        with self.assertRaises(TypeError):
            Rectangle(3, '5')
        with self.assertRaises(TypeError):
            Rectangle(3, 5.0)
        with self.assertRaises(TypeError):
            Rectangle(4, [5, 7, 8])

    def test_height_setter_for_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -5)

    def test_x_setter_wrong_type(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5, '3')
        with self.assertRaises(TypeError):
            Rectangle(3, 5, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(4, 7, [5, 7, 8])

    def test_x_setter_for_neg_values(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 5, -4)
        with self.assertRaises(ValueError):
            Rectangle(4, 50, -100)

    def test_y_setter_wrong_type(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 8, '3')
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 7, (1, 2))
        with self.assertRaises(TypeError):
            Rectangle(4, 7, 9, [5, 7, 8])

    def test_y_setter_for_neg_value(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 5, 2, -4)
        with self.assertRaises(ValueError):
            Rectangle(4, 50, 4, -100)

    def test_y_setter_when_none(self):
        """Test setter when none is passed"""

        with self.assertRaises(TypeError):
            Rectangle(2, 3, 5, None)

    def test_rect_area(self):
        r1 = Rectangle(3, 7)
        r2 = Rectangle(12, 6, 1, 2, 12)
        r3 = Rectangle(4, 5, 2, 3)

        self.assertEqual(r3.area(), 20)
        self.assertEqual(r2.area(), 72)
        self.assertEqual(r1.area(), 21)

    def test_area_with_value_passed(self):
        r2 = Rectangle(12, 6, 1, 2, 12)
        with self.assertRaises(TypeError):
            r2.area(6)

    def test_str_method(self):
        """ Checks the str special method """

        r2 = Rectangle(12, 6, 1, 2, 12)
        r1 = Rectangle(3, 7)
        r3 = Rectangle(4, 5, 2, 3)

        self.assertEqual(str(r2), '[Rectangle] (12) 1/2 - 12/6')
        self.assertEqual(str(r1), '[Rectangle] (33) 0/0 - 3/7')
        self.assertEqual(str(r3), '[Rectangle] (34) 2/3 - 4/5')

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

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_rect_dictionary(self):
        """ checks if the square dictionary is correct """
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(13, 5, 6, 9, 10)

        self.assertEqual(r1.to_dictionary(),
                        {'id': 30, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        self.assertEqual(r2.to_dictionary(),
                        {'id': 10, 'width': 13, 'height': 5, 'x': 6, 'y': 9})

    def check_rect_if_dictionary(self):
        """ checks if to dictionary returns a dictionary """
        r1 = Rectangle(10, 2, 1, 50, 13)
        r_dict = r1.to_dictionary()

        self.assertIsInstance(type(r_dict), dict)

    def test_save_to_file(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_create_class_method(self):
        d1 = {"id": 3, "width": 1, "height": 1, "x": 0, "y": 0}
        d2 = {"id": 9, "width": 3, "height": 5, "x": 3, "y": 0}
        r_1 = Rectangle.create(**d1)
        r_2 = Rectangle.create(**d2)
        self.assertEqual(str(r_1), "[Rectangle] (3) 0/0 - 1/1")
        self.assertEqual(str(r_2), "[Rectangle] (9) 3/0 - 3/5")
        self.assertIsNot(r_1, r_2)
        self.assertNotEqual(r_1, r_2)
        self.assertIs(type(r_1), type(r_2))

    def test_load_from_file_if_not_present(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        r_1 = Rectangle(4, 1, 4, 2)
        r_2 = Rectangle(3, 2, 2, 2)
        ls = [r_1, r_2]
        Rectangle.save_to_file(ls)
        nw_ls = Rectangle.load_from_file()
        self.assertIs(type(nw_ls), list)
        self.assertIs(type(nw_ls[0]), Rectangle)
        self.assertEqual(len(nw_ls), 2)
        self.assertEqual(str(nw_ls[0]), str(r_1))
        self.assertIsNot(nw_ls[0], ls[0])


    def test_basic_display(self):
        
        r = Rectangle(2, 3, 0, 0, 1)
        expected_display = "##\n##\n##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)


    def test_display_xy(self):
        """Testing the display method with x and y"""
        r = Rectangle(2, 2, 2, 2, 1)
        expected_display = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new = StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected_display)
