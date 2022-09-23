#!/usr/bin/python3
""" Testing module for Base Class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base! """

    def test_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

if __name__ == "__main__":
    unittest.main()
