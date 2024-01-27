#!/usr/bin/python3
"""
    make a fetch request
"""

import urllib.request


url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":    
    with urllib.request.urlopen(url) as response:
        data = response.read()
        utf8_content = data.decode('utf-8')
        print("Body response:")
        print("    - type:", type(data))
        print("    - content:", data)
        print("    - utf8 content:", utf8_content)
