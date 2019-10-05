#!/usr/bin/python3
"""
The module receive two arguments

and say the name complete concatenate
"""


def say_my_name(first_name, last_name=""):
    """ Function receives the argument and return
    name_Complete = first_name + last_name
    """
    if type(first_name) is not str:
        """ Verify if is string """
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        """ Verify if is string """
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
