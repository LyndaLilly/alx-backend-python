#!/usr/bin/env python3
""" this is the basics """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this is the task_wait_random n times with the specified max_delay.
    """
    tsks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tsks)]
