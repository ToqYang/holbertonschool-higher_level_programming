#!/usr/bin/python3
""" All class to JSON """


class Student:
    """ Contain the definition about student """

    def __init__(self, first_name, last_name, age):
        """ Constructor of the Student
            Initializes values
            first_nmae, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary description in Dictionary
            verify if sype is str, then return only list
            otherwise return all dictionary of the class"""
        if (type(attrs) == list and all(type(element) == str
                                        for element in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
