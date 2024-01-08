#!/usr/bin/env python3
'''
Module test_client: test module for client.py
'''
import unittest
from unittest.mock import Mock, patch, PropertyMock
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

    @parameterized.expand([
        ('url_one', {'repos_url': 'http://url_one.com'}),
        ('url_two', {'repos_url': 'http://url_two.com'})
        ])
    def test_public_repos_url(self, url_name, url):
        ''' test method fo GitHubOrgClient._public_repos_url '''
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=url)):
            result = GithubOrgClient(url_name)._public_repos_url

            self.assertEqual(result, url.get('repos_url'))


if __name__ == '__main__':
    unittest.main()
