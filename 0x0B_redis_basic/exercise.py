#!/usr/bin/env python3
"""
0x0B. Redis basic
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        return data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        get function
        """
        if key:
            if fn:
                return fn(self._redis.get(key))
            return self._redis.get(key)
