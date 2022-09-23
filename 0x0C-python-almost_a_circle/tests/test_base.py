#!/usr/bin/python3
""" Testing module for Base Class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base! """

    def test_id_given(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_empty(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_id_string(self):
        b3 = Base("hi")
        self.assertEqual(b3.id, "hi")

if __name__ == "__main__":
    unittest.main()
