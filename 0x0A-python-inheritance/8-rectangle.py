#!/usr/bin/python3
""" Make Rectangle class """


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


class Rectangle(BaseGeometry):
    """ Make a Rectangle from Basegeometry """
    def __init__(self, width, height):
        """ Constructor that verify the values and after the assign"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
