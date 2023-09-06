#!/usr/bin/python3
"""
script that takes in a URLsends a request to the URL
displays the value of the X-Request-Id variable
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
