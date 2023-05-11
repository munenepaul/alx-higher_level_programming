#!/usr/bin/python3
if __name__ == "__main__":
    """Print all non-private names defined by the imported module"""
    import hidden_4 as my_hidden_module
    names = dir(my_hidden_module)
    for name in names:
        if name[:2] != "__":
            print(name)
