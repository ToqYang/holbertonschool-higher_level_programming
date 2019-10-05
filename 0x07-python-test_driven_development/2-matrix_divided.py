#!/usr/bin/python3
"""
The matrix contain two arguments
matrix = 2d elements hard
div = Number to divide the matrix
"""


def matrix_divided(matrix, div):
    """
    Verify the if the dividend is 0 if is float or int
    Look the matrix is a list and if it has the same size
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    a = [[round((element / div), 2) for element in lit_ma]for lit_ma in matrix]

    ma_resolved = a.copy()

    return ma_resolved
