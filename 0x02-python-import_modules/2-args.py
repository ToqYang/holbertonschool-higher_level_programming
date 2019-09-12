#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{:d} arguments.".format(len(sys.argv) - 1))
else:
    for i, j in enumerate(sys.argv):
        if i != 0 and j != 0:
            print("{}: {}".format(i, j))
