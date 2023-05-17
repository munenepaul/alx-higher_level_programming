#!/usr/bin/python3
def update_dictionary(some_dictionary, new_key, new_value):
    """Replaces or adds a key/value pair in a dictionary."""
    updated_dict = dict(some_dictionary)
    updated_dict[new_key] = new_value
    return updated_dict
