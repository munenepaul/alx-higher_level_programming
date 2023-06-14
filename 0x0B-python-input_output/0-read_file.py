#!/usr/bin/python3
"""
Contains the read_file function
"""


def write_file(filename="", text=""):
     """""reads a text file(UTF8) and prints it to stdout"""
     with open(filename, "w", encoding="utf-8") as file:
         file.write(text)
         return len(text)
