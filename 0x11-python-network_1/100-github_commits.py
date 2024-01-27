#!/usr/bin/python3
#using request library to send request to github api and show last user commits

import requests
import sys


repo = sys.argv[1]
user = sys.argv[2]

url = f"https://api.github.com/repos/{user}/{repo}/commits"
if __name__ == "__main__":
    r = requests.get(url)
    try:
        response = r.json()
        for i in range(10):
            sha = response[i].get('sha')
            author = response[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except ValueError:
        print("Not a valid JSON")
