#!/usr/bin/env python3
'''
Module 1: Executing multiple coroutines at the same time with async
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    async function that return a list of all delays(float values)
    params
    n(int)
    max_delay(int)
    '''
    delays = []

    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
