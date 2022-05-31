#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """"function that reads a text file
    (UTF8) and prints it to stdout"""
    with open('my_file_0.txt', encoding='utf-8') as f:
        print(f.read(), end='')
