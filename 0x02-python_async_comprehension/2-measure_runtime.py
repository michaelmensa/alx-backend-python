#!/usr/bin/env python3
'''
Module 2: run time for four parallel comprehensions
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    coroutine that will execute async_comprehension 4 times in parallel
    using asyncio.gather.
    should measure the total runtime and return it
    '''
    start_t = time.time()

    task = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*task)

    return time.time() - start_t
