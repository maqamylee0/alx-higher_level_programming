#!/usr/bin/python3
"""
script that takes your GitHub credentials uses the GitHub API to display the Id
"""

from sys import argv
import requests

if __name__ == '__main__':
    response = requests.get("https://api.github.com/user",
                            auth=(argv[1], argv[2]))
    data = response.json()
    id = data.get('id')
    print(id)
