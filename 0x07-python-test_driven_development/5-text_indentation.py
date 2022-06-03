#!/usr/bin/python3
""" module for import text indentation"""


def text_indentation(text):
    """ split strings
    Text: text to split"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for symbol in ".:?":
        text = (symbol + "\n\n").join(
            [line.strip("") for line in text.split(symbol)])
    print("{}".format(text), end="")
