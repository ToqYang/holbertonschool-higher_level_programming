#!/usr/bin/python3
class Rectangle:
    """ Make a empty class """

    def __init__(self, width=0, height=0):
        """ Constructor of variables """
        self.width = width
        self.height = height

    def __del__(self):
        """ Destructor of the class """
        print("Bye rectangle...")

    def __str__(self):
        """
        Store the string with the rectangle
        """
        rect_draw = ""

        if self.width == 0 or self.height == 0:
            return rect_draw

        for x in range(0, self.height):
            rect_draw += "#" * self.width

            if x >= self.height - 1:
                continue
            rect_draw += "\n"

        return rect_draw

    def __repr__(self):
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

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

    def area(self):
        """
        The ecuations for recatangle is:
        A_Rectangle = Height * width
        """
        if self.width == 0 or self.height == 0:
            return 0

        return self.height * self.width

    def perimeter(self):
        """
        The perimeter, This I get with the sum of your sides
        """
        if self.width == 0 or self.height == 0:
            return 0

        return ((self.height + self.width) * 2)
