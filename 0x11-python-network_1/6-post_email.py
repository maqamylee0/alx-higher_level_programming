#!/usr/bin/python3
#using request library to post email value

import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print(r.text)
