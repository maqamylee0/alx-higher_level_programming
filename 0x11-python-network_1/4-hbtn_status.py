#!/usr/bin/python3
#using request library to fetch

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    content = r.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
