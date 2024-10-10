#!/usr/bin/env python3
"""
A type-annotated function `sum_mixed_list` which takes a list `mxd_lst`
of integers and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    function that takes a list of integers and floats
    and returns their sum as a float.
    """
    sum: float = 0
    for val in mxd_lst:
        sum = sum + val
    return sum
