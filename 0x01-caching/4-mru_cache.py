#!/usr/bin/python3
"""implementing the LIFO caching algorithm"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A LIFOCache class to implement caching algo"""
    def __init__(self):
        """Initialize the LIFOCache using super class"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Set attr on the cache data"""
        if key and item and key not in self.cache_data.keys():
            if len(self.cache_data) < self.MAX_ITEMS:
                self.queue.append(key)
                self.cache_data[key] = item
            else:
                recent = self.queue.pop()
                del self.cache_data[recent]
                self.queue.append(key)
                self.cache_data[key] = item
                print(f"DISCARD: {recent}")
        elif key and item and key in self.cache_data.keys():
            self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Get the value of key in cache_data"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
