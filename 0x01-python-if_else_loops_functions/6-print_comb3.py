#!/usr/bin/python3
if __name__ == "__main__":
    for num1 in range(8):
        for num2 in range(10):
            if num1 < num2:
                print("{:d}{:d}, ".format(num1, num2), end="")
    print(89)
