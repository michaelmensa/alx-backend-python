#!/usr/bin/env python3
'''
Module 0: the basics of async.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    async coroutine that takes an int: maxdelay(10) and waits for a random
    delay and returns the value in float
    '''

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
