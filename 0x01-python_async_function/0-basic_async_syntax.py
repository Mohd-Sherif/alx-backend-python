#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
(`max_delay`, with a default value of 10) named `wait_random`
that waits for a random delay between 0 and `max_delay`
(included and float value) seconds and eventually returns it.
"""

import random


async def wait_random(max_delay=10):
    """
    waits for a random delay between 0 and `max_delay`
    seconds and eventually returns it.
    """
    return random.uniform(0, max_delay)
