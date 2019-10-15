#!/usr/bin/python3
""" Inherits from list to the class MyList """


class MyList(list):
    """ Inherits from list for can be return how list """
    def print_sorted(self):
        """ Print the list sorted of manner ascending"""
        print(sorted(self))
