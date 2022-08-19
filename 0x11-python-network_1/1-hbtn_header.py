#!/usr/bin/python3
"""
Returns a formatted response using urllib
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as data:
        print(data.info().get("X-Request-Id"))
