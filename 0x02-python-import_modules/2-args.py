#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        for i, j in enumerate(sys.argv):
            if i != 0 and j != 0:
                print("{}: {}".format(i, j))
    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i, j in enumerate(sys.argv):
            if i != 0 and j != 0:
                print("{}: {}".format(i, j))
