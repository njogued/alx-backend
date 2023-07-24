#!/usr/bin/env python3
"""Create a function that takes two int arguments and retuns index as tuple"""


def index_range(page, page_size):
    """Create and return a tuple of indexes"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
