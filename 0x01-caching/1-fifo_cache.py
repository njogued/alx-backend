#!/usr/bin/env python3
"""FIFOCache algorithm that inherits from BaseCaching"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initializing the FIFOclass"""
        super().__init__()
        self.queue = deque()  # Queue to track order of insertion

    def put(self, key, item):
        """Assign the value(item) to the key"""
        if key and item:
            self.queue.append(key)
            if len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                oldest = self.queue.popleft()
                del self.cache_data[oldest]
                self.cache_data[key] = item
                print(f"DISCARD: {oldest}\n")

    def get(self, key):
        """Return the item corresponding to the key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
