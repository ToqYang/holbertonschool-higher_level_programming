#!/bin/usr/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits of the Rectangle class that in turn
        inherits of the Base class

        Args:
            Rectangle (Class): Class that inherits the attributes and methods
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor that call to Rectangle class
            for initialize the values

        Args:
            size (int): Is the height and width of a square
            x (int): Position in horizontal
            y (int): Position in vertical
            id (int): Number idenficator of the object
        """
        super().__init__(size, size, x, y, id)

    # Dimensions of a Square
    @property
    def size(self):
        """ Get the value of the size """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the value of the variable size

            Args:
                value (int): Receive the value and after the filter
                the methods width and height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ Print for the user

            Return:
                  [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.height)
