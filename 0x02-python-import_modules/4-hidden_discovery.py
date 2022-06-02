#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = [word for word in dir(hidden_4) if not (word.startswith('__'))]
    print('\n'.join(names))
