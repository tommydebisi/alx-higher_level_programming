#!/usr/bin/python3
"""
    This script sends a POST request to the passed URL
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    query_st = {"email": sys.argv[2]}
    data = parse.urlencode(query_st).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf8"))
