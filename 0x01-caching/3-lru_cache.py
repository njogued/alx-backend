#!/usr/bin/python3
"""implementing the LIFO caching algorithm"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A LIFOCache class to implement caching algo"""
    def __init__(self):
        """Initialize the LIFOCache using super class"""
        super().__init__()

    def put(self, key, item):
        """Set attr on the cache data"""
        if key and item and key not in self.cache_data.keys():
            if len
