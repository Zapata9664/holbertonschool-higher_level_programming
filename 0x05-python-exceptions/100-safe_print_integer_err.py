#!/usr/bin/python3
"""Module for print integuer"""


def safe_print_integer_err(value):
    """Write a function that prints an integuer"""
    import sys
    try:
        print("{:value}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
