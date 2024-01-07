#!/usr/bin/env python3
'''
Module test_client: test module for client.py
'''
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' class to test client.GithubOrgClient
    '''

    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        ''' method to test client.org and returns the correct
        value
        '''
        github_client = GithubOrgClient(org_name)
        result = github_client.org
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == '__main__':
    unittest.main()
