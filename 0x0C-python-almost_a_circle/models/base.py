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

    # Save json to a file
    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to file the JSON of the passed objects

            Args:
                cls: Object class
                list_objs: Dictionary with attributes to convert in dictionary
        """
        filename = cls.__name__ + ".json"
        new_list = []

        with open(filename, "w") as fil:
            if list_objs is None:
                fil.write(new_list)

            for x in list_objs:
                new_list.append(x.to_dictionary())

            json_str = ""
            json_str = cls.to_json_string(new_list)

            fil.write(json_str)

    # Json string to dict
    def from_json_string(json_string):
        """ Convert the Json to string and verify if is empty or None

        Args:
            json_string: Received a list of dictionary of attributes

        Return:
           List represented by json_string
        """
        new_list = []

        if not json_string or json_string is None:
            return new_list

        new_list.append(json_string)
        return new_list

    # Dcitionary instance
    def create(cls, **dictionary):
        """ Make a dictionary based in the instance

        Args:
            cls: Object instance
            **dictionary: Dictionary with the class

        Return:
           All attributes passed
        """

    def load_from_file(cls):
        """ Load a file with the information of the instance

        Args:
            cls: Object Instance

        Return:
           Information with a list of instances
        """
