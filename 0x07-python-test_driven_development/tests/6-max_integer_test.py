#!/usr/bin/python3
"""module tests"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class Test6_Max_Integer(unittest.TestCase):
    """unitests for class 6-max integer"""
    def test_ints_unorderd(self):
        """tests for integers only list"""
        list1 = [1, 2, 7, 3]
        self.assertEqual(max_integer(list1, 7))

    def test_repeat(self):
        """checks max with repeated numbers"""
        list2 = [1, 2, 2]
        self.assertEqual(max_integer(list2, 2))

    def test_ordered(self):
        """checks max in ordered list"""
        list3 = [1, 2, 3]
        self.assetEqual(max_integer(list3, 3))

if __name__ == '__main__':
    unittest.main()
