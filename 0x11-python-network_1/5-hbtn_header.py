#!/usr/bin/python3
#using request library to get header value

import requests
import sys

url = sys.argv[1]
if __name__ == "__main__":
    r = requests.get(url)
    x_request_id = r.headers.get('X-Request-Id')
    print(x_request_id)
