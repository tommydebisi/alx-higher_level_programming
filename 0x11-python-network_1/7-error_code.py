#!/usr/bin/python3
"""
    This script takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter, and finally displays
    the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    with requests.get(argv[1]) as response:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
