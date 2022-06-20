#!/usr/bin/python3
"""Module for safely function"""


def safe_function(fct, *args):
    """Write a function that executes a function safely."""
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
