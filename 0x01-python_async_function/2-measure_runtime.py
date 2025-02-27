#!/usr/bin/env python3
""" this is the basics """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ this is the measure """
    sts = time()

    run(wait_n(n, max_delay))

    dn = time()

    return (dn - sts) / n
