#!/bin/usr/python3
""" Base class """


class Base:
    """ Base class for go to define your features

        _nb_objects = Private variable that store the objects
        id = Number identifier of the object
    """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """ Constructor of the base class

            self = Is the object that already make the class
            id = Is a identifier of the object
        """

        if id is None:
            # Verify if the id is empty and assign the number of objects
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        if id is not None:
            # Otherwise assign the value received
            self.id = id
