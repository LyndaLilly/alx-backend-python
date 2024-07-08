#!/usr/bin/env python3
""" this is the async func """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ this is the tasks """
    tsk = create_task(wait_random(max_delay))
    return tsk
