#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(0, (0, 0))
print(my_square)

print("--")

my_square = Square(3, (2, 2))
my_square.my_print()
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)
