#!/usr/bin/python3
"""
    This script takes in a URL and an email address, sends a POST request
    to the passed URL with the email as a parameter, and finally displays
    the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    post_dict = {'email': argv[2]}
    with requests.post(argv[1], data=post_dict) as response:
        print(response.text)
