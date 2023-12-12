#!/usr/bin/env python3
'''
Module 0: Coding my first Async Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator():
    '''
    coroutine that takes no arguments. will loop 10 times,
    each time, wait asynchronously for 1 sec, then yield a random number
    between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
