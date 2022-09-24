#!/usr/bin/python3
"""
    This script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    api = "https://api.github.com/user"
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    r = requests.get(api, auth=auth)

    if r.status_code >= 400:
        print(None)
    else:
        try:
            json = r.json()
            print(json.get("id"))
        except Exception:
            print(None)
