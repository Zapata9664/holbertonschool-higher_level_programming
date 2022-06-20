#!/usr/bin/python3
"""Moodule for add attribute"""


def add_attribute(obj, attribute, value):
    """Write a function that adds a new attribute to
    an object if it’s possible"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
