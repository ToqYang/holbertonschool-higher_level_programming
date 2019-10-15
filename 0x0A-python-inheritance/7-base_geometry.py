#!/usr/bin/python3
""" Make Base Geometry class """


class BaseGeometry:
    """ Empty class """
    def area(self):
        """ Function until now print the exception
            in case of that the functiont doesn't work"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Verify if is a integer and if the value is
            less than 0 """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
