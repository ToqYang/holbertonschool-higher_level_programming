#!/usr/bin/python3
""" Look if is the type of the class """


def is_kind_of_class(obj, a_class):
    """ Comparate if is instace of inherits from something class  """
    if isinstance(obj, a_class):
        return True

    return False
