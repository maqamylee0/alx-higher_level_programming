#!/usr/bin/python3
"""test module for rectangle"""


import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for rectangle class and methods"""
    
    def setUp(self):
        """reset id for method"""
        Base.__nb_instance = 0

    def test_init(self):
        """test initialisation"""
        test1 = Rectangle(2, 2)
        self.assertEqual(test1.width, 2)
        self.assertEqual(test1.height, 2)

    def test_init_whx(self):
        """check width, height, and x"""
        test2 = Rectangle(2, 3, 4)
        self.assertEqual(test2.width, 2)
        self.assertEqual(test2.height, 3)
        self.assertEqual(test2.x, 4)

    def test_init_whxy(self):
        """checks width, height, x and y"""
        test3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(test3.width, 1)
        self.assertEqual(test3.height, 2)
        self.assertEqual(test3.x, 3)
        self.assertEqual(test3.y, 4)

    def test_init_whxy_id(self):
        """check width, height, x y and id"""
        test4 = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(test4.width, 1)
        self.assertEqual(test4.height, 2)
        self.assertEqual(test4.x, 3)
        self.assertEqual(test4.y, 4)
        self.assertEqual(test4.id, 1)

    def test_getters_and_setters(self):
        """checks for getters and setters"""
        test5 = Rectangle(1, 2, 3, 4)
        self.assertEqual(test5.width, 1)
        self.assertEqual(test5.height, 2)
        self.assertEqual(test5.x, 3)
        self.assertEqual(test5.y, 4)

        test5.height = 5
        test5.width = 6
        test5.x = 7
        test5.y = 8

        self.assertEqual(test5.width, 6)
        self.assertEqual(test5.height, 5)
        self.assertEqual(test5.x, 7)
        self.assertEqual(test5.y, 8)

if __name__ == '__main__':
    unittest.main()
