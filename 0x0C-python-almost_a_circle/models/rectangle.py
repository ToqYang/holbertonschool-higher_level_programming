#!/usr/bin/python3
"""  Module that Use the class base for make a Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Make the base class of a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of the class Rectangle

            Args:
                width = Amplitude of the Rectangle
                height = Ceil of the hight of the Rectangle
                x = Coordinates in x (Horizontal)
                y = Coordinates in y (Vertical)
                id = Number identifier of the object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Dimensions of the Rectangle
    @property
    def width(self):
        """ Get the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the value of the variable width

            Args:
                value (int): Receive the value and after the filter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Get the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the value of the variable height

            Args:
                value (int): Receive the value and after the filter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # Positions of the Rectangle
    @property
    def x(self):
        """ Get the value of the x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the value of the variable x

            Args:
                value (int): Receive the value and after the filter
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Get the value of the y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the value of the variable y

            Args:
                value (int): Receive the value and after the filter
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    # Operations for the figures
    def area(self):
        """ Get the area of a rectangle

            Return:
                  Area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """ Represent of manner graphical the HxW with # """
        for x in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ Print for the user
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.width) + "/" + str(self.height)
