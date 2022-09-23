#!/usr/bin/python3
"""
    This script fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen, Request

req = Request("https://alx-intranet.hbtn.io/status")
with urlopen(req) as response:
    data = response.read()

# decode gets the string representation of the message
print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf-8 content: {} \
      ".format(type(data), data, data.decode("utf-8").strip("\t")))
