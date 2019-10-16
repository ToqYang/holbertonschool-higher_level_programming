#!/usr/bin/python3
""" Read a file  """


def number_of_lines(filename=""):
    """ Received the filename for it can does a syscall for read the file
        Return: Counter of the lines"""
    count = 0
    with open(filename, mode="r", encoding="utf-8") as fil:
        for line in fil:
            count += 1

    return count
