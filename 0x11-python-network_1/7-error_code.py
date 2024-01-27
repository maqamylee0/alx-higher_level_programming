#!/usr/bin/python3
"""
using request library to send request and handle error
"""
import requests
import sys

url = sys.argv[1]

if __name__ == "__main__":
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
