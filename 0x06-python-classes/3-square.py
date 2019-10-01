#!/usr/bin/python3
class Square:
    """ Defining a Square class """
    def __init__(self, size=0):
        """ Constructor square class """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
         """ Return area of a square """
        return self.__size * self.__size
