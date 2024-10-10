#!/usr/bin/env python3
"""
A type-annotated function `add` that takes a float `a`
and a float `b` as arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    return a + b


print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
