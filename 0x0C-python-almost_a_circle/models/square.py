#!/usr/bin/python3
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

    # Print features of the class
    def __str__(self):
        """ Print for the user

            Return:
                  [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/"\
            + str(self.y) + " - " + str(self.height)

    # Print attributes more easiest
    def update(self, *args, **kwargs):
        """ Receive all arguments of the class

            Args:
                *args: Receive no-keyword argument and the store
                       - With set attribute compare with a list and
                         we set the attributes in args

            **kwargs: Dictionary with keys and values
                     - Throught of a loop, We travel in the key
                       after in the value of his value
                       after, we with setattr, we set the values
        """
        my_attr = ["id", "size", "x", "y"]
        count = 0

        for arg in args:
            setattr(self, my_attr[count], arg)
            count += 1

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Dictionary of the class
    def to_dictionary(self):
        """" Dictionary representation of a Square

        Return:
           id, size, x, y
        """
        my_attri = ["id", "size", "x", "y"]
        val_attr = 0
        dic_ret = {}

        for i in range(len(my_attri)):
            val_attri = getattr(self, my_attri[i])
            dic_ret[my_attri[i]] = val_attri

        return dic_ret
