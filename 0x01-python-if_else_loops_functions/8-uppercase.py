#!/usr/bin/python3
def to_uper(character):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - (ord('a') - ord('A')))
            print("{:s}".format(c), end='')
            print("")
