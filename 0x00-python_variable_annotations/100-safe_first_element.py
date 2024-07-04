#!/usr/bin/env python3
""" this is duck type """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# These are types of the elements that the inputs are unknown
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ this safe first element """
    if lst:
        return lst[0]
    else:
        return None
