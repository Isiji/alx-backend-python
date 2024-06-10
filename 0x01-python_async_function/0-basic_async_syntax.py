#!/usr/bin/python3

"""Basic async syntax module"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time