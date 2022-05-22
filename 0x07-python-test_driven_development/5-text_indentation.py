#!/usr/bin/python3
"""function that prints a text with 2 new lines
 after each of these characters:
 ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines
 after each of these characters:
 ., ? and :"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    cringes = ".?:"

    text = text.strip()

    for cringe in cringes:
        text = text.replace(cringe, "{}\n\n".format(cringe))
    print("\n".join([li.strip() for li in text.split("\n")]), end="")
