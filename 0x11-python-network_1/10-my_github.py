#!/usr/bin/python3
"""
using request library to send request to github api and show user id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


username = sys.argv[1]
password = sys.argv[2]

url = "https://api.github.com/user"
if __name__ == "__main__":
    auth_user = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth_user)
    try:
        response = r.json()
        if response == {}:
            print("None")
        else:
            print("{}".format(response.get("id")))
    except ValueError:
        print("Not a valid JSON")
