#!/usr/bin/python3
import json
""" Json representations Object to a text file """


def save_to_json_file(my_obj, filename):
    """Save the json in a file
       Receive the filename and the object"""
    with open(filename, mode="w", encoding="utf-8") as fil:
        return json.dump(my_obj, fil)
