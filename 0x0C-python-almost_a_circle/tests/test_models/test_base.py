#!/bin/usr/python3
""" Class for proves the things """

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ The class does the test

       Args:
          unittest.TestCase: Inherits the methods for proves the tests.
    """

    def test_ins(self):
        """" Verify if the type of the object is the same """
        self.assertIs(type(Base()), Base)

    def test_id(self):
        """ Verify the values of the constructor
            if is empty or there something
        """
        self.assertEqual(Base(13).id, 13)
        self.assertEqual(Base().id, 1)

if __name__ == "__main__":
    """ Entry point for look the unittest """
    unittest.main()
