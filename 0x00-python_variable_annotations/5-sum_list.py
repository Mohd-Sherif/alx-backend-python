#!/usr/bin/env python3
"""
A type-annotated function `sum_list` which takes a list `input_list`
of floats as argument and returns their sum as a float.
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    function that returns the sum of all values in the passed list.
    """
    sum: float = 0
    for val in input_list:
        sum = sum + val
    return sum
