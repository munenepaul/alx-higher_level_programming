#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None

    for char in sentence:
        length += 1
        first_char = char
        break

    return (length, first_char)
