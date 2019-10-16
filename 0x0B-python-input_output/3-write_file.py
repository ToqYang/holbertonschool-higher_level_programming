#!/usr/bin/python3
""" Write in a file determined  """


def write_file(filename="", text=""):
    """ Write in a file with the arguments received
        String = filename
        String = text
    """
    with open(filename, mode="w", encoding="utf-8") as fil:
        return fil.write(text)
