#!/usr/bin/python3
""" Read a file in UTF8  """


def read_file(filename=""):
    """ Received the filename for it can does a syscall for read the file """
    with open(filename, mode="r", encoding="utf-8") as fil:
        rd_Txt = fil.read()
        print(rd_Txt, end="")
