#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_1_num(self):
        self.assertEqual(max_integer([1]), 1)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)

    def test_strList(self):
        self.assertRaises(TypeError, max_integer(["hi", "hello", "bye"]))
    
    def test_floatList(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
