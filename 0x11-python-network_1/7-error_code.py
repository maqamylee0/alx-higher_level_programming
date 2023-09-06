#!/usr/bin/python3
"""
script taking in a URL,sends a request to it and displays the body of response
"""

from sys import argv
import requests

if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code > 399:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
