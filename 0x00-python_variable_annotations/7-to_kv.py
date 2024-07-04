#!/usr/bin/env python3
""" this the complex types of tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this takes a string k and an int OR float v as arguments
    returns a tuple.
    """

    return (k, v**2)
