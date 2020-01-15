#!/usr/bin/python3
""" Error code #1 """
import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":

    try:
        res = requests.get(sys.argv[1])
        print(res)
    except HTTPError as e:
        print("Error code: {}".format(e))
