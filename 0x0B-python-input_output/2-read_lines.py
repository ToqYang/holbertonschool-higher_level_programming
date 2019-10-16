#!/usr/bin/python3
""" Read a file  """


def read_lines(filename="", nb_lines=0):
    """ Received the filename for it can does a syscall for read the file
        print number lines about nb_lines
        if is 0 print all"""
    if (nb_lines > 0):
        count = 0
        with open(filename, mode="r", encoding="utf-8") as fil:
            for line in fil:
                if nb_lines <= count:
                    break
                print(line, end="")
                count += 1

    else:
        with open(filename, mode="r", encoding="utf-8") as fil:
            read_data = fil.read()
            print(read_data, end="")
