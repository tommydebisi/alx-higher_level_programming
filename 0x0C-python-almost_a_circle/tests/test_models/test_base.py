"""
Test cases for base class
"""

from models import base
import unittest
import json
Base = base.Base



class TestBaseId(unittest.TestCase):
    """Test for functionality of base classes"""

    def setUp(self):
        self.bs = Base()

    def test_nb_object_is_private(self):
        with self.assertRaises(AttributeError):
            print(self.bs.__nb_object)

    def test_for_id_if_passed(self):
        bs = Base(10)
        self.assertEqual(bs.id, 10)

    def test_for_id_if_not_passed(self):
        self.assertEqual(self.bs.id, 1)
        bs_1 = Base()
        self.assertEqual(bs_1.id, 2)

    def test_to_json_string_if_none_is_passed(self):
        json_string = self.bs.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_if_dict_empty_is_passed(self):

        json_string = self.bs.to_json_string({})
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):

        list_dict = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        j_string = self.bs.to_json_string(list_dict)
        self.assertEqual(j_string, json.dumps(list_dict))
        self.assertIs(type(j_string), str)

    def test_from_json_string(self):
        list_dict = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        j_string = self.bs.to_json_string(list_dict)
        py_obj = self.bs.from_json_string(j_string)
        self.assertIs(type(py_obj), list)
        self.assertIs(type(py_obj[0]), dict)
        self.assertEqual(py_obj, list_dict)

    def test_from_json_string_none(self):
        list_dict = None
        j_string = self.bs.to_json_string(list_dict)
        py_obj = self.bs.from_json_string(j_string)
        self.assertIs(type(py_obj), list)
        self.assertEqual(py_obj, [])

    def test_from_json_string_empty(self):
        list_dict = []
        j_string = self.bs.to_json_string(list_dict)
        py_obj = self.bs.from_json_string(j_string)
        self.assertIs(type(py_obj), list)
        self.assertEqual(py_obj, [])

    def test_if_args_more_than_one(self):
        with self.assertRaises(TypeError):
            Base(3, 5)