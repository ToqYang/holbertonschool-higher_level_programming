#!/usr/bin/python3
class Square:
    """ Defining a Square class """
    def __init__(self, size=0):
        """ Constructor square class """
        self.size = size

    @property
    def size(self):
        """ Getter property """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property
        value: Variable for verify correct value

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return area of a square """
        return self.__size * self.__size
