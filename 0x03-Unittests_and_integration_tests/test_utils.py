#!/usr/bin/env python3
'''
Module test_utils: test for utils.py
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Any, Mapping, Sequence
from utils import access_nested_map, get_json, memoize
import requests


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

    @parameterized.expand([
        ({}, ('a')),
        ({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test access_nested_map for exceptions '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' test class for testing get_json '''

    @parameterized.expand([
        ("http://example.com", {'payload': True}),
        ("http://holberton.io", {'payload': False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        ''' test method for testing utils.get_json '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    ''' test class for testing memoize decorator '''

    def test_memoize(self):
        ''' test method for testing utils.memoize '''
        class TestClass:
            ''' test class '''
            def a_method(self):
                ''' a_method '''
                return 42

            @memoize
            def a_property(self):
                ''' a_property '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_obj:
            obj = TestClass
            result = obj.a_property
            result2 = obj.a_property
            self.assertEqual(result, result2)

            mock_obj.assert_called_once


if __name__ == '__main__':
    unittest.main()
