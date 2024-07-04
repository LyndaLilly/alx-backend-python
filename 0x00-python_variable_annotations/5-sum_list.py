#!/usr/bin/env python3
""" this is the complex list types """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
    this takes a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(input_list)
