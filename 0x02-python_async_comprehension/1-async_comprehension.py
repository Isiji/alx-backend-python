#!/usr/bin/python3
"""async comprehension"""

import asyncio
import random
from typing import List
from importlib import import_module as using

async_generator = using("0-async_generator").async_generator

async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing over async_generator"""
    return [i async for i in async_generator()]