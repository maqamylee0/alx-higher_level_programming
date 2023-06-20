#!/usr/bin/python3
"""test module for square"""


import json
import unittest
from unittest.mock import patch
from models.base import Base
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests for square class and methods"""
    
    def setUp(self):
        """reset id for method"""
        Base.__nb_instance = 0

    def test_init(self):
        """test initialisation"""
        test1 = Square(2)
        self.assertEqual(test1.size, 2)

    def test_init_whx(self):
        """check width, height, and x"""
        test2 = Square(2, 3, 4)
        self.assertEqual(test2.size, 2)
        self.assertEqual(test2.x, 3)
        self.assertEqual(test2.y, 4)

    def test_init_whxy(self):
        """checks width, height, x and y"""
        test3 = Square(1, 2, 3, 4)
        self.assertEqual(test3.size, 1)
        self.assertEqual(test3.x, 2)
        self.assertEqual(test3.y, 3)
        self.assertEqual(test3.id, 4)

    def test_getters_and_setters(self):
        """checks for getters and setters"""
        test5 = Square(1, 2, 3, 4)
        self.assertEqual(test5.size, 1)
        self.assertEqual(test5.x, 2)
        self.assertEqual(test5.y, 3)

        test5.size = 6
        test5.x = 7
        test5.y = 8

        self.assertEqual(test5.size, 6)
        self.assertEqual(test5.x, 7)
        self.assertEqual(test5.y, 8)

    def test_area(self):
        """checks area"""
        test6 = Square(2)
        self.assertEqual(test6.area(), 4)

    def test_str(self):
        """check strigify"""
        test7 = Square(4, 2, 1, 12)
        output = '[Square] (12) 2/1 - 4'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test7, end="")
        self.assertEqual(mocked_output.getvalue(), output)

    def test_display_square(self):
        """test display"""
        test8 = Square(4)
        output = ("####\n" +
                  "####\n" +
                  "####\n" +
                  "####\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test8.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_attributes(self):
        """test attribute error"""
        with self.assertRaises(TypeError):
            test9 = Square("1")
        with self.assertRaises(TypeError):
            test9 = Square(1, "3")
        with self.assertRaises(TypeError):
            test9 = Square(1, 2, "3")
        with self.assertRaises(TypeError):
            test9 = Square(1, 2, "3", 4)
        with self.assertRaises(TypeError):
            test9 = Square(1.3, 3.4)
        with self.assertRaises(TypeError):
            test9 = Square(1, 3, 2.4, 9)
        with self.assertRaises(ValueError):
            test9 = Square(0)
        with self.assertRaises(ValueError):
            test9 = Square(-1)
        with self.assertRaises(ValueError):
            test9 = Square(1, -2)
        with self.assertRaises(ValueError):
            test9 = Square(0, 2)
        with self.assertRaises(ValueError):
            test9 = Square(1, 2, -3)

    def test_display_without_y(self):
        """check for display without y"""
        test10 = Square(3, 2)
        output = ("  ###\n" + "  ###\n" + "  ###\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test10.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_display_with_cord(self):
        """add all cordinates"""
        test11 = Square(3, 2, 1)
        output = ("\n  ###\n" + "  ###\n" + "  ###\n")
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            test11.display()
        self.assertEqual(mocked_output.getvalue(), output)

    def test_update_args(self):
        """checks for updating with args"""
        test12 = Square(1, 2, 3, 4)
        self.assertEqual(test12.size, 1)
        self.assertEqual(test12.x, 2)
        self.assertEqual(test12.y, 3)
        self.assertEqual(test12.id, 4)

        test12.update(5, 6, 7, 8)
        self.assertEqual(test12.size, 6)
        self.assertEqual(test12.x, 7)
        self.assertEqual(test12.y, 8)
        self.assertEqual(test12.id, 5)

        test12.update(89)
        self.assertEqual(test12.id, 89)

        test12.update(1, 2, 3)
        self.assertEqual(test12.size, 2)
        self.assertEqual(test12.x, 3)
        self.assertEqual(test12.id, 1)

        test12.update(4, 5)
        self.assertEqual(test12.size, 5)
        self.assertEqual(test12.id, 4)

    def test_update_kwargs(self):
        """change values with dictionary"""
        test13 = Square(2, 3, 4, 5)
        self.assertEqual(test13.size, 2)
        self.assertEqual(test13.x, 3)
        self.assertEqual(test13.y, 4)
        self.assertEqual(test13.id, 5)

        test13.update(**{'id': 4})
        self.assertEqual(test13.id, 4)

        test13.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.size, 1)

        test13.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(test13.id, 89)
        self.assertEqual(test13.size, 1)
        self.assertEqual(test13.x, 2)
        self.assertEqual(test13.y, 3)

    def test_create(self):
        """check creating copy"""
        test15 =Square.create(**{ 'id': 89 })
        output = '[Square] (89) 0/0 - 1'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test15, end="")
        self.assertEqual(mocked_output.getvalue(), output)

    def test_create_size(self):
        """test with size"""
        test16 = Square.create(**{ 'id': 89, 'size': 1 })
        output = '[Square] (89) 0/0 - 1'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test16, end="")
        self.assertEqual(mocked_output.getvalue(), output)

    def test_create_size_x(self):
        """test with size and x"""
        test17 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        output = '[Square] (89) 2/0 - 1'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test17, end="")
        self.assertEqual(mocked_output.getvalue(), output)
    
    def test_create_size_x_y(self):
        """test with size x and y"""
        test19 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3})
        output = '[Square] (89) 2/3 - 1'
        with patch('sys.stdout', new=StringIO()) as mocked_output:
            print(test19, end="")
        self.assertEqual(mocked_output.getvalue(), output)

    def test_save_to_file(self):
        """save to file"""
        test20 = [Square(1), Square(2)]
        Square.save_to_file(Square, test20)
        from_file = Square.load_from_file(Square)
        self.assertEqual(len(test20), len(from_file))
        for i in range(len(test20)):
            self.assertEqual(from_file[i].to_dictionary(), test20[i].to_dictionary())

    def test_save_to_file_empty(self):
        """save empty list to file"""
        test21 = Square.save_to_file(Square, [])
        recs = Square.load_from_file(Square)
        self.assertEqual(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
