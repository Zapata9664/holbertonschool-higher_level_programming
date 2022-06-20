#!/usr/bin/python3
""" Module for class MyInt """


class MyInt(int):
    """Write a class MyInt that inherits from int"""

    def __eq__(self, other):
        """Compare equal"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """compare not equal"""
        return (super().__eq__(other))
