#!/usr/bin/python3
""" Write in a file determined  """


def append_write(filename="", text=""):
    """ Write in a file but this appends at the end with the arguments received
        String = filename
        String = text
    """
    with open(filename, mode="a", encoding="utf-8") as fil:
        return fil.write(text)
