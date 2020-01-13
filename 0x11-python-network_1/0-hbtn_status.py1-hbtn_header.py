#!/usr/bin/python3
""" What's my status? """
import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as res:
    con = res.read()
    enc = con.decode('utf-8')
    namclas = type(con)
    
    print("Body response:")
    print("\t- type: {}".format(namclas))
    print("\t- content: {}".format(con))
    print("\t- utf8 content: {}".format(enc))
      
