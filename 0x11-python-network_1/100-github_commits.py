#!/usr/bin/python3
#using request library to send request to github api and show last user commits

import requests
import sys


repo = sys.argv[1]
user = sys.argv[2]

url = "https://api.github.com/repos/OWNER/REPO/commits"
if __name__ == "__main__":
    payload = {"owner": user,
                "repo": repo
                }
    r = requests.get(url,  data=payload)
    try:
        response = r.json()
        if response == []:
            print("None")
        else:
            for i in response:
                sha = i['sha']
                author = i['commit']['author']['name']
                print("{}: {}".format(sha, author_name))
    except ValueError:
        print("Not a valid JSON")
