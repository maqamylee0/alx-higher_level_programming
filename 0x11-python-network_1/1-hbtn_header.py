#!/usr/bin/python3
#take request url and display header value

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

