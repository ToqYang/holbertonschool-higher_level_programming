#!/usr/bin/python3
import json
""" Return data object Python represented by a JSON """


def from_json_string(my_str):
    """ We receive a string about JSON and deserialization to python object"""
    return json.loads(my_str)
