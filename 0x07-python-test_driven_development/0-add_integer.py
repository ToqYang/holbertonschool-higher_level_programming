#!/usr/bin/python3
"""
The module sum integer and give the result

and return the sum of the two integers
"""


def add_integer(a, b=98):
    """ Sum integer a + b
    b = 98 Initialized
    """

    if isinstance(a, float):
        """ Cast in case of be float """
        a = int(a)
    if isinstance(b, float):
        """ Cast in case of be float """
        b = int(b)

    if type(a) != int:
        """ Verify if is integer """
        raise TypeError("a must be an integer")

    if type(b) != int:
        """ Verify if is integer """
        raise TypeError("b must be an integer")

    return a + b
