#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random
from asyncio import async_generator


async def async_generator() -> async_generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10