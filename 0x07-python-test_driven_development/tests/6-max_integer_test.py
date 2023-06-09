#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unitests for class 6-max integer"""
    def test_ints_unorderd(self):
        """tests for integers only list"""
        list1 = [1, 2, 7, 3]
        self.assertEqual(max_integer(list1), 7)

    def test_repeat(self):
        """checks max with repeated numbers"""
        list2 = [1, 2, 2]
        self.assertEqual(max_integer(list2), 2)

    def test_ordered(self):
        """checks max in ordered list"""
        list3 = [1, 2, 3]
        self.assertEqual(max_integer(list3), 3)

    def test_empty(self):
        """check empty list"""
        list4 = []
        self.assertEqual(max_integer(list4), None)

    def test_str(self):
        """check string"""
        list5 = ["emma"]
        self.assertEqual(max_integer(list5), 'emma')

    def test_single(self):
        """check single element list"""
        list6 = [1]
        self.assertEqual(max_integer(list6), 1)


if __name__ == '__main__':
    unittest.main()
