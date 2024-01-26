#!/usr/bin/python3
#make a fetch request

import urllib.request


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "main":    
    with urllib.request.urlopen(url) as response:
        data = response.read()
        utf8_content = body.decode('utf-8')
        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", utf8_content)
