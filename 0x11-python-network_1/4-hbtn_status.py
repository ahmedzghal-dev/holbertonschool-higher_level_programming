#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests

req = requests.get('https://intranet.hbtn.io/status')
data = req.text
data_type = type(data)

print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
