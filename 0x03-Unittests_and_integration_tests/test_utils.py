#!/usr/bin/env python3
'''
Module test_utils: test for utils.py
'''
import unittest
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    test class for testing access_nested_map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, exp_result: Any) -> Any:
        ''' test_access_nested_map function '''
        nest = access_nested_map(nested_map, path)
        self.assertEqual(nest, exp_result)


if __name__ == '__main__':
    unittest.main()
