#!/usr/bin/python3
def no_c(my_string):
    updated_str = ''.join([char for char in my_string if char.lower() != 'c'])
    return updated_str
