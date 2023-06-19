#!/usr/bin/python3
"""Base class unitests"""


from models import base
from models.base import Base
import json


class TestBaseClass(unittest.TestCase):
    """base class tests"""
    def setUp(self):
        """reset class variable n each run"""
        Base._Base__nb_objects = 0

    def test_module_doc(self):
        """checks for documentation"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """check for class dicumentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_instance_id(self):
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
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string_none(self):
        """check with None as id"""
        self.assertEqual(json_string, [])
        
    if __name__ == '__main__':
        unittest.main()

