#!/usr/bin/python3
"""defining save to json filr"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
