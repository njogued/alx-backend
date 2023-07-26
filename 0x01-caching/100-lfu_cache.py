#!/usr/bin/python3
"""implementing the LIFO caching algorithm"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A LIFOCache class to implement caching algo"""
    def __init__(self):
        """Initialize the LIFOCache using super class"""
        super().__init__()
        self.queue = []
        self.lru = {}

    def put(self, key, item):
        """Set attr on the cache data"""
        if key and item and key not in self.cache_data.keys():
            if len(self.cache_data) < self.MAX_ITEMS:
                self.queue.append(key)
                self.lru[key] = 1
                self.cache_data[key] = item
            else:
                most_frequent = min(self.lru.values())
                frequents = [key for key, value in self.lru.items() if value
                             == most_frequent]
                if len(frequents) == 1:
                    self.queue.remove(frequents[0])
                    del self.cache_data[frequents[0]]
                    del self.lru[frequents[0]]
                    self.queue.append(key)
                    self.cache_data[key] = item
                    self.lru[key] = 1
                    print(f"DISCARD: {frequents[0]}")
                elif len(frequents) > 1:
                    for recent_key in self.queue:
                        if recent_key in frequents:
                            break
                    self.queue.remove(recent_key)
                    del self.cache_data[recent_key]
                    del self.lru[recent_key]
                    self.queue.append(key)
                    self.lru[key] = 1
                    self.cache_data[key] = item
                    print(f"DISCARD: {recent_key}")
        elif key and item and key in self.cache_data.keys():
            self.queue.remove(key)
            self.queue.append(key)
            self.lru[key] += 1
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
            self.lru[key] += 1
            return self.cache_data[key]
