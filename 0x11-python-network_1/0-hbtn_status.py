# 0-hbtn_status.py

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:\n\n    - type: <class 'bytes'>\n    - content: {}\n    - utf8 content: {}".format(
          i  type(data), data.decode('utf-8')))
