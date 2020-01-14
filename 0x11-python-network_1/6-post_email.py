#!/usr/bin/python3
""" POST an email #1 """
import requests
import sys

if __name__ == "__main__":

    dat = {}
    dat['email'] = sys.argv[2]

    req = requests.post(sys.argv[1], data=dat)
    print(req.text)
