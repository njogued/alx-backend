#!/usr/bin/python3
"""A caching system without a limit"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Setattr the key to item in self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get the value of the item corresponding to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
