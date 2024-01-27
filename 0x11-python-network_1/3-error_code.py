#!/usr/bin/python3
"""
deal with errors
"""
import sys
import urllib.request
import urllib.error


url = sys.argv[1]

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url, data=data) as response:
            data2 = response.read()
            utf_8_content = data2.decode('utf-8')
            print(utf_8_content)
    except urllib.error.HTTError as e:
        print("Error code: {}".format(e.code))
