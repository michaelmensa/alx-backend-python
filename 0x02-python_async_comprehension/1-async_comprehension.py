#!/usr/bin/env python3
'''
Module 1: coding my first async comprehensions
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    coroutine will collect 10 random numbers usin an async comprehension
    over async_generator, then return 10 random numbers
    '''
    result = [i async for i in async_generator()]
    return result
