#!/usr/bin/python3
""" All class to JSON """


def class_to_json(obj):
    """ Return dictionary description in JSON"""
    return obj.__dict__
