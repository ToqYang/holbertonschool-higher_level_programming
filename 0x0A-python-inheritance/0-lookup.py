#!/usr/bin/python3
""" Print all the attributes and methods of an object """


def lookup(obj):
    """ Return a list with all attributes  and method
        of the object passed how argument """
    return dir(obj)
