#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asc = ord(char)
        if 97 <= asc <= 122:
            print("{:c}".format(asc - 32), end="")
        else:
            print("{:c}".format(asc), end="")
    print()
