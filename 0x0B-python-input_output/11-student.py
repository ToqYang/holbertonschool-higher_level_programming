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

    def to_json(self):
        """ Return dictionary description in Dictionary """
        return self.__dict__
