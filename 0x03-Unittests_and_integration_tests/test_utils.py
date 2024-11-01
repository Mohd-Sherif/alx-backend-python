#!/usr/bin/env python3
"""
Test for access_nested_map function
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test the access_nested_map method.
        Args:
            nested_map (Dict): A dictionary that may have nested dictionaries
            path (List, tuple, set): Keys to get to the required value in the
                                     nested dictionary
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)
