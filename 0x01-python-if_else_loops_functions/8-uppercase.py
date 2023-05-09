#!/usr/bin/python3
def uppercase(s):
    new = ""
    for c in s:
        if 'a' <= c <= 'z':
            new += chr(ord(c) - 32)
        else:
            new += c
            print(new)
