#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU class
    """

    def __init__(self):
        """
        constructor
        """
        self.usedKey = {}
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            # modify the time and change the next newer value
            if key not in self.usedKey:
                self.usedKey[key] = 1
            else:
                self.usedKey[key] += 1

            # add the new item
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            tmpDict = {}
            for _key, _value in self.usedKey.items():
                if str(_value) not in tmpDict and _key is not key:
                    tmpDict[str(_value)] = _key

            tmpSorted = sorted(tmpDict.items())
            discard_key = tmpSorted[0][1]

            # del key in used and cache data
            del self.cache_data[discard_key]
            del self.usedKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None

        # modify the used
        self.usedKey[key] += 1

        return self.cache_data[key]
