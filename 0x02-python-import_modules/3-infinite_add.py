#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumval = 0
    for x, j in enumerate(sys.argv):
        if x != 0 and j != 0:
            sumval += int(sys.argv[x])
    print("{:d}".format(sumval))
