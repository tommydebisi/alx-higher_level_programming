#!/usr/bin/python3
from importlib.abc import Loader
my_module = Loader.load_module(__file__, "./hidden_4.pyc")
print(dir(my_module))