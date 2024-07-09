#!/usr/bin/env python3

""" this is the asynchoronous """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ this is the asynchoronous  """
    sax = [x async for x in async_generator()]
    return sax
