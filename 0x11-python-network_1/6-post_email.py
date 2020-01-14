#!/usr/bin/python3
""" POST an email #1 """
import requests
import sys

if __name__ == "__main__":

    data = {}
    data['email'] = sys.argv[2]

    req = request.post(sys.argv[1], data)
    print(req)
