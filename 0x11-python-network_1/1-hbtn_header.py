#!/usr/bin/python3
""" Response header value """
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.headers.get('X-Request-Id'))
