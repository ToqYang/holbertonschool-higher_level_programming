#!/usr/bin/python3
""" Search API """
import sys
import requests

if __name__ == "__main__":

    req = requests.get('http://0.0.0.0:5000/search_user')

    dat = {}
    dat['q'] = sys.argv[1]

    req = requests.post(sys.argv[1], data=dat)
    print(req.text)

    
