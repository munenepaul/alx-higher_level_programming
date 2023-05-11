#!/usr/bin/pythoni3
def magic_calculation(a, b):
    """Match bytecode provided by Holberton School"""
    from magic_calculation_102 import add, sub
    if a < b:
        c = sum([a, b] + list(range(4, 6)))
        return c
    else:
        return a - b
