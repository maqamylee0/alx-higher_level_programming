#!/usr/bin/python3
#post data

import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        data2 = response.read()
        utf_8_content = data2.decode('utf-8')
        print(utf_8_content)
