#!/usr/bin/python3
""" Contain the fucntion that find if this are the same class """


def is_same_class(obj, a_class):
    """ We received the object and the class to comparate """
    return type(obj) == a_class
