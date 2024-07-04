#!/usr/bin/env python3

""" this is the mixed list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  this returns the sum as a float. """
    return float(sum(mxd_lst))
