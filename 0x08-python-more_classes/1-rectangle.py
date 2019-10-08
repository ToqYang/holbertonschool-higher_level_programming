#!usr/bin/python3
class Rectangle:
    """ Make a empty class """
    def __init__(self, width=0, height=0):
        """ Constructor of variables """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Return value: height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Verify if is correct value
            ValueError: If the height < 0
            TypeError: If the value not is integer
            Return: Private variable changed
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Return value: height """
        return self.__width

    @width.setter
    def width(self, value):
        """ Verify if is correct value
        ValueError: If the width < 0
        TypeError: If the value not is integer
        Return: Private variable changed
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
