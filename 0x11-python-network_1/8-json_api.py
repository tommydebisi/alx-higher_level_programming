#!/usr/bin/python3
"""
    This script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    st = argv[1] if len(argv) > 1 else ""
    post_dic = {'q': st}

    r = requests.post("http://0.0.0.0:5000/search_user", data=post_dic)

    try:
        dic_val = r.json()
        if dic_val:
            print("[{}] {}".format(dic_val.get('id'), dic_val.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
