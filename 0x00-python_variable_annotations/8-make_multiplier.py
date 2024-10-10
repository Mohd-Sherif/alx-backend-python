#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes
a float `multiplier` as argument and returns a function
that multiplies a float by `multiplier`.
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    function that takes a float as argument
    and returns a function that multiplies a float by it.
    """
    def multiplier_function(val: float) -> float:
        return val * multiplier
    return multiplier_function
