#!/usr/bin/python3
"""
    This script  takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
import urllib
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
