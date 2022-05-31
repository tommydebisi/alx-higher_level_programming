#!/usr/bin/python3
if __name__ == "__main__":
    for char in range(97, 123):
        if char == 101 or char == 113:
            continue
        print("{:c}".format(char), end="")
