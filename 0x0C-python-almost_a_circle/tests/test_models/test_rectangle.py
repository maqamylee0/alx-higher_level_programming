#!/usr/bin/python3
"""test module for rectangle"""


import json
import unittest
from unittest.mock import patch
from models.base import Base
from io import StringIO
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

    def test_area(self):
        """checks area"""
        test6 = Rectangle(2, 2)
        self.assertEqual(test6.area(), 4)

    def test_str(self):
        """check strigify"""
        test7 = Rectangle(4, 6, 2, 1, 12)
        output = '[Rectangle] (12) 2/1 - 4/6'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test7, end="")
        self.assertEqual(mocked_output.getvalue(), output)

    def test_display_rectangle(self):
        """test display"""
        test8 = Rectangle(4, 6)
        output = ("####\n" +
                  "####\n" +
                  "####\n" +
                  "####\n" +
                  "####\n" +
                  "####\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test8.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_attributes(self):
        """test attribute error"""
        with self.assertRaises(TypeError):
            test9 = Rectangle("1", 3)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, "3")
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            test9 = Rectangle(1.3, 3.4)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 3, 2.4, 9)
        with self.assertRaises(TypeError):
            test9 = Rectangle(1, 4, 5, 5.1)
        with self.assertRaises(ValueError):
            test9 = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            test9 = Rectangle(-1, 3)
        with self.assertRaises(ValueError):
            test9 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            test9 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            test9 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            test9 = Rectangle(1, 3, 3, -4)

    def test_display_without_y(self):
        """check for display without y"""
        test10 = Rectangle(3, 2, 3)
        output = ("   ###\n" + "   ###\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test10.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_display_with_cord(self):
        """add all cordinates"""
        test11 = Rectangle(3, 2, 3, 1)
        output = ("\n   ###\n" + "   ###\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test11.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_update_args(self):
        """checks for updating with args"""
        test12 = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(test12.width, 1)
        self.assertEqual(test12.height, 2)
        self.assertEqual(test12.x, 3)
        self.assertEqual(test12.y, 4)
        self.assertEqual(test12.id, 1)

        test12.update(5, 6, 7, 8, 5)
        self.assertEqual(test12.width, 6)
        self.assertEqual(test12.height, 7)
        self.assertEqual(test12.x, 8)
        self.assertEqual(test12.y, 5)
        self.assertEqual(test12.id, 5)

        test12.update(89)
        self.assertEqual(test12.id, 89)

        test12.update(1, 2, 3)
        self.assertEqual(test12.width, 2)
        self.assertEqual(test12.height, 3)
        self.assertEqual(test12.id, 1)

        test12.update(4, 5)
        self.assertEqual(test12.width, 5)
        self.assertEqual(test12.id, 4)

        test12.update(1, 2, 3, 4)
        self.assertEqual(test12.width, 2)
        self.assertEqual(test12.height, 3)
        self.assertEqual(test12.x, 4)
        self.assertEqual(test12.id, 1)

    def test_update_kwargs(self):
        """change values with dictionary"""
        test13 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(test13.width, 1)
        self.assertEqual(test13.height, 2)
        self.assertEqual(test13.x, 3)
        self.assertEqual(test13.y, 4)
        self.assertEqual(test13.id, 5)

        test13.update(**{'id': 4})
        self.assertEqual(test13.id, 4)

        test13.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.width, 1)

        test13.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.width, 1)
        self.assertEqual(test13.height, 2)

        test13.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.width, 1)
        self.assertEqual(test13.height, 2)
        self.assertEqual(test13.x, 3)

        test13.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.width, 1)
        self.assertEqual(test13.height, 2)
        self.assertEqual(test13.x, 3)
        self.assertEqual(test13.y, 4)

    def test_to_dictionary(self):
        """checks for dictionary of object"""
        test14 = Rectangle(10, 2, 1, 9)
        output = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test14.to_dictionary()
        self.assertEqual(mocked_output.getvalue(), output)

if __name__ == '__main__':
    unittest.main()
