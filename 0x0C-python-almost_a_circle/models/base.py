#!/bin/usr/python3
""" Base class """
import json


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

    # Convert Json to string
    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert JSON to a string readable

        Args:
            list_dictionaries: Bring the dictionary of the class converted

        Return:
           JSON string representation of that class
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
