#!/usr/bin/python3
"""
using request library to send request and handle params
"""
import requests
import sys


q = "" if len(sys.argv == 1) else sys.argv[1]
url = "http://0.0.0.0:5000/search_user"
if __name__ == "__main__":
    payload = {"q" : q}
    r = requests.post(url, data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
