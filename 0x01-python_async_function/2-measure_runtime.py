#!/usr/bin/env python3
'''
Module 3: Measuring the runtime
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    coroutine that measure the total execution time for wait_n
    returns total_time/n
    '''
    start_t = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_t = time.time()

    total_time = end_t - start_t

    return total_time / n
