#!/usr/bin/python3
""" Verify if is a class inherits directly or indirectly """


def inherits_from(obj, a_class):
    """ Received the object and a_class and the comaparate """
    return not type(obj) == a_class and isinstance(obj, a_class)
