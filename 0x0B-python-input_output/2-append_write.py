#!/usr/bin/python3
"""append a string at the end of a text file"""


def append_write(filename="", text=""):
    """"appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open('file_append.txt', 'a', encoding='utf-8') as f:
        f.write(text)
        return(len(text))
