#!/usr/bin/python3
""" Testing module for Base Class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base! """

    def test_id_empty(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

if __name__ == "__main__":
    unittest.main()
