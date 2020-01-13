#!/usr/bin/python3
""" Response header value """
import urllib.request
import sys

urlhol = sys.argv[1]

req = urllib.request.Request(urlhol)
with urllib.request.urlopen(req) as res:
    print(res.headers.get('X-Request-Id'))
