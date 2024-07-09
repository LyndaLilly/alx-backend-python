#!/usr/bin/env python3

""" this is the asynchoronous """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ this is the asynchoronous run time """
    st = time()
    todos = [async_comprehension() for x in range(4)]
    await gather(*todos)
    ed = time()
    return (ed - st)
