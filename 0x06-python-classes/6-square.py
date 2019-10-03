#!/usr/bin/python3
class Square:
    """ Defining a Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Constructor square class """
        self.size = size
        self.position = position
 
    def area(self):
       """ Return area of a square """
        return self.__size * self.__size
 
    def my_print(self):
        """ Print the # """
        if self.__size is 0:
            print()
        else:
            if self.position[1] is not 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
 
    @property
    def size(self):
        """ Getter property """
        return self.__size
 
    @size.setter
    def size(self, value):
        """
        Setter property
        value: Variable for verify correct value """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
 
    @property
    def position(self):
        """ Getter property """
        return self.__position
 
    @position.setter
    def position(self, value):
        """                                                           Setter property
           value: Variable for verify correct value """

        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
