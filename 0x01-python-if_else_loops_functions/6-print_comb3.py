#!/usr/bin/python3
if __name__ == "__main__":
    for num1 in range(8):
        for num2 in range(10):
            if num1 < num2:
                print(f"{num1:d}{num2:d}, ", end="")
    print(89)
