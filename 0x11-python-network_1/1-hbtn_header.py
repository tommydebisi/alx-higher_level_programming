#!/usr/bin/python3
"""
    This script sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        print(response.getheader("X-Request-Id"))
