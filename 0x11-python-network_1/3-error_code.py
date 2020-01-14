#!/usr/bin/python3
""" What's my status? """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":

    request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as ans:
            print(ans.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
