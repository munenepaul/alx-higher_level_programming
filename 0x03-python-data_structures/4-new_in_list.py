#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at specific index without modifying the whole list"""
    if 0 <= idx < len(my_list):
        copy = my_list[:]
        copy[idx] = element
        return copy
    else:
        return my_list
