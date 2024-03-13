#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unit test for Square model"""

    def test_initialization_success(self):
        s1 = Square(13)
        s2 = Square(14)
        self.assertEqual(s1.id, 13)
        self.assertEqual(s2.id, 14)

    def test_initialization_without_arguments(self):

        self.assertRaises(TypeError, Square)

if __name__ == '__main__':
    unittest.main()
