#!/usr/bin/python3
"""
The module calculate the size of a square ()

and print the square
"""


def print_square(size):
    """
    Print the a square about your size
    Size: Dimensions of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    x = 0

    for x in range(size):
        print("#" * size)
