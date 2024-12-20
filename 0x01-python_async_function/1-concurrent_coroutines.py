#!/usr/bin/env python3
"""
Import wait_random from the previous python file
that you’ve written and write an async routine called
wait_n that takes in 2 int arguments (in this order)
n and max_delay. You will spawn wait_random n times
with the specified max_delay.

wait_n should return the list of all the delays
(float values). The list of the delays should be in
ascending order without using sort() because of concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert each completed delay into the correct position
        # in the list (insertion sort style)
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
