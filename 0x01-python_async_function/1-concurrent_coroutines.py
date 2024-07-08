#!/usr/bin/env python3
""" this is the basics """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this is the wait_random n times with the specified max_delay.
    """
    tsk = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tsk)]
