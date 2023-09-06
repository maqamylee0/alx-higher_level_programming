#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request as purl
from sys import argv
import sys

if __name__ == '__main__':
    if len(argv) > 1:
        with purl.urlopen(argv[1]) as pool:
            headers = dict(pool.info())
            if 'X-Request-Id' in headers:
                print(headers['X-Request-Id'])
    else:
        sys.exit()
