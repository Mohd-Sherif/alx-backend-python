#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n. The code is nearly
identical to wait_n except task_wait_random
is being called.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

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
