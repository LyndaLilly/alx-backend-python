#!/usr/bin/env python3
'''
    This is the basics
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    this gets a random delay btwn 0 and max_delay
    seconds and eventually returns it
    """
    dl = random.uniform(0, max_delay)
    await asyncio.sleep(dl)
    return dl
