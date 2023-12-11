#!/usr/bin/env python3
'''
Module 1: Executing multiple coroutines at the same time with async
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    async function that return a list of all delays(float values)
    params
    n(int)
    max_delay(int)
    '''
    delays = []

    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
