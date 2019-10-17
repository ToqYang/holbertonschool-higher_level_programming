#!/usr/bin/python3
import json
""" Return data object Python represented by a JSON """


def load_from_json_file(filename):
    """ We receive a filename with JSON and deserialization to python object"""
    with open(filename) as fil:
        return json.load(fil)
