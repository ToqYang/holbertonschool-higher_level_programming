#!/bin/usr/python3
""" Class for proves the things Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """ The class does the test of the Rectangle

       Args:
          unittest.TestCase: Inherits the methods for proves the tests.
    """
    def test_class(self):
        """ Verify is is subclass and if is th same type """
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIs(type(Rectangle(10, 20)), Rectangle)

    def test_attr(self):
        """ Look if ht attributes of the width, height, x, y, id """
        rect = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 12)

    def test_raise(self):
        """ Raise exception each one with yours messages because:

            If the input not is an integer, raise the TypeError
            If width or height is under or equals 0, raise the ValueError
            If x or y is under 0, raise the ValueError exception
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(10, 10).width = -10

        with self.assertRaises(ValueError):
            Rectangle(10, 10).height = -10

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10).x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 10).y = -5

    def test_area(self):
        """ It put to proves the area of the Rectangle """
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(9, 9, 0, 0, 23).area(), 81)

    #def test_display(self):
     #   """ """
        #self.assertEqual(Rectangle(2, 2).display)

    def test_str(self):
        """ """
        self.assertEqual(print(Rectangle(4, 6, 2, 1, 12)), '[Rectangle] (12) 2/1 - 4/6')

if __name__ == "__main__":
    """ Entry point for look the unittest """
    unittest.main()
