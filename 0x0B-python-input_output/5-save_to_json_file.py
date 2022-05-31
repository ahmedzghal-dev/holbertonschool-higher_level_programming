#!/usr/bin/python3
"""write an object to text file"""


import json
"""import module"""


def save_to_json_file(my_obj, filename):
    """write an Object to a text file
    using a JSON representation"""
    return(json.dumps(my_obj))
