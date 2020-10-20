#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    wait_random function
    """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
