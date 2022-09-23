#!/usr/bin/python3
"""
    This script takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib
import sys

if __name__ == "__main__":
    new_dict = {'email': sys.argv[2]}
    parsed = urllib.parse.urlencode(new_dict)

    # POST data should be in bytes
    parsed = parsed.encode('ascii')

    request = urllib.request.Request(sys.argv[1], parsed)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
