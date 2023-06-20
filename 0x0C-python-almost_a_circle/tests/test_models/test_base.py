#!/usr/bin/python3
"""Base class unitests"""


import unittest
import json
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """base class tests"""
    def setUp(self):
        """reset class variable n each run"""
        Base.__nb_objects = 0

    def test_class_doc(self):
        """check for class dicumentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_init(self):
        """check for ids of instances"""
        test1 = Base()
        self.assertEqual(test1.id, 1)

        test2 = Base()
        self.assertEqual(test2.id, 2)

        test3 = Base(6)
        self.assertEqual(test3.id, 6)

    def test_to_json_string(self):
        """check if json_to_string works"""
        list1 = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 1}
        list2 = {'id': 2, 'width': 1, 'height': 3, 'x': 1, 'y': 3}
        test4 = [list1, list2]
        json_string = Base.to_json_string(test4)
        self.assertTrue(type(json_string) is str)
        json_object = json.loads(json_string)
        self.assertEqual(json_object, test4)

    def test_to_json_string_none(self):
        """check with None as id"""
        test5 = Base.to_json_string(None)
        self.assertEqual(test5, '[]')

    def test_from_json_string_none(self):
        """check with None as id"""
        test6 = Base.from_json_string(None)
        self.assertEqual(test6, [])

    def test_to_json_string_empty(self):
        """checks empty lsit"""
        test7 = Base.to_json_string([])
        self.assertEqual(test7, '[]')

    def test_from_json_string_empty(self):
        """checks empty list from json"""
        test8 = Base.from_json_string(None)
        self.assertEqual(test8, [])

    def test_from_json_string(self):
        """checks expected value"""
        test9 = '[{"id": 1, "width":3, "height": 4, "x": 3, "y": 1}]'
        expected = [{'id': 1, 'width': 3, 'height': 4, 'x': 3, 'y': 1}]
        self.assertEqual(Base.from_json_string(test9), expected)
        
    if __name__ == '__main__':
        unittest.main()

